from django.shortcuts import render, HttpResponseRedirect
from .models import Hotel
from django.db.models import Q



def room_filter(hotel, places=None):
    for hr in Hotel.objects.mongo_aggregate([{'$match': {'name': hotel['name']}},
                                                   {'$project':
                                                        {'room':
                                                             {'$filter':
                                                                  {'input': {'$map': {'input': '$room',
                                                                                          'as': 'room',
                                                                                          'in': {
                                                                                              'number': '$$room.number',
                                                                                              'places': '$$room.places',
                                                                                              'price': '$$room.price',
                                                                                              'description': '$$room.description',
                                                                                              'img': '$$room.img',
                                                                                              'reserved': {
                                                                                                  '$filter': {
                                                                                                      'input': '$$room.reserved',
                                                                                                      'as': 'reserved',
                                                                                                      'cond': {}
                                                                                                  }
                                                                                              }
                                                                                          }}},
                                                                   'as': 'room',
                                                                   'cond': {'$eq': ['$$room.places', places]}
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
    if places:
        hr_filter = room_filter(hotel=hotel,
                                places=int(places),)
    #     filter = hotel_rooms.filter(Q(hr_places=places) &
    #                                 (Q(reserveddates__check_in__gt=check_in) &
    #                                  Q(reserveddates__check_in__lt=check_out) |
    #                                  Q(reserveddates__check_out__gt=check_in) &
    #                                  Q(reserveddates__check_out__gt=check_out))).distinct()
    #     if request.method == 'POST':
    #         add_srv = request.POST.get('additional_services', 'RO')
    #
    #
    template = "catalog_app/hotel_card.html"
    context = {'hotel': hotel,
               'room_filter': hr_filter,
               'places': places}
    return render(request, template, context)
