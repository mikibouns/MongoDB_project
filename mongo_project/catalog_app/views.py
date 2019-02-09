from django.shortcuts import render
from .models import Hotel
from django.db.models import Q


def get_hotels():
    return Hotel.objects.mongo_find()


def catalog_page(request):
    hotels = get_hotels()
    template = "catalog_app/catalog.html"
    context = {'hotels': hotels}
    return render(request, template, context)


def hotel_card_page(request, pk):
    pass
    # hotel_card = HotelCard.objects.get(id=pk)
    # hotel_rooms = HotelRoom.objects.filter(hr_hotel__id=pk)
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
    # template = "catalog_app/hotel_card.html"
    # context = {'hotel': hotel_card,
    #            'rooms': hotel_rooms,
    #            'room_filter': filter,
    #            'check_in': check_in,
    #            'check_out': check_out,
    #            'places': places}
    # return render(request, template, context)