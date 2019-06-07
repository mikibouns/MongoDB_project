from django.shortcuts import render
from .models import Hotel
import time
import datetime


def room_filter(hotel, places=None, check_in=None, check_out=None):
    if check_in:
        check_in = time.mktime(datetime.datetime.strptime(check_in, "%Y-%m-%d").timetuple())
        check_in = {'$or': [{'$gt': [check_in, '$$reserved.check_out']},
                             {'$lt': [check_in, '$$reserved.check_in']}]}
    if check_out:
        check_out = time.mktime(datetime.datetime.strptime(check_out, "%Y-%m-%d").timetuple())
        check_out = {'$or': [{'$gt': [check_out, '$$reserved.check_out']},
                              {'$lt': [check_out, '$$reserved.check_in']}]}
    if places:
        places = {'$eq': ['$$room.places', int(places)]}
    for hr in Hotel.objects.mongo_aggregate([{'$match': {'name': hotel['name']}},
                                                   {'$project':
                                                        {'room':
                                                             {'$filter':
                                                                  {'input': {'$map': {'input': '$room',
                                                                                          'as': 'room',
                                                                                          'in': {
                                                                                              'category': '$$room.category',
                                                                                              'number': '$$room.number',
                                                                                              'places': '$$room.places',
                                                                                              'price': '$$room.price',
                                                                                              'description': '$$room.description',
                                                                                              'img': '$$room.img',
                                                                                              'reserved': {
                                                                                                  '$filter': {
                                                                                                      'input': '$$room.reserved',
                                                                                                      'as': 'reserved',
                                                                                                      'cond': {'$and': [check_in,
                                                                                                                       check_out]}
                                                                                                  }
                                                                                              }
                                                                                          }}},
                                                                   'as': 'room',
                                                                   'cond':{'$and': [places,
                                                                                    {'$ne': ['$$room.reserved', []]}]}
                                                                   }
                                                              }
                                                         }
                                                    }
                                                   ]):
        return hr['room']

#-----------------------------------------------------------------------------------------------------------------------


def catalog_page(request):
    hotels = Hotel.objects.mongo_find()
    template = "catalog_app/catalog.html"
    context = {'hotels': hotels}
    return render(request, template, context)


def hotel_page(request, short_name):
    hotel = Hotel.objects.mongo_find_one({'short_name': short_name})
    check_in = (request.GET.get('check-in', None))
    check_out = (request.GET.get('check-out', None))
    places = (request.GET.get('places', None))
    hr_filter = hotel['room']
    if places or check_in or check_out:
        hr_filter = room_filter(hotel=hotel,
                                places=places,
                                check_in=check_in,
                                check_out=check_out,)
    #     if request.method == 'POST':
    #         add_srv = request.POST.get('additional_services', 'RO')

    template = "catalog_app/hotel_card.html"
    context = {'hotel': hotel,
               'room_filter': hr_filter,
               'places': places,
               'check_in': check_in,
               'check_out': check_out}
    return render(request, template, context)
