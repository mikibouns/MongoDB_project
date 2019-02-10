from django.shortcuts import render, HttpResponseRedirect
from .models import Hotel
from django.db.models import Q


def get_hotels(hotel_name=False):
    if hotel_name:
        return Hotel.objects.mongo_find_one({'short_name': hotel_name})
    return Hotel.objects.mongo_find()


def catalog_page(request):
    hotels = get_hotels()
    template = "catalog_app/catalog.html"
    context = {'hotels': hotels}
    return render(request, template, context)


def hotel_page(request, short_name):
    hotel = get_hotels(short_name)
    # check_in = (request.GET.get('check-in', None))
    # check_out = (request.GET.get('check-out', None))
    # places = (request.GET.get('places', None))
    # filter = hotel_rooms
    # if check_in and check_out and places:
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
    context = {'hotel': hotel}
    return render(request, template, context)
