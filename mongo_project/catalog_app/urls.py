from django.urls import path
from . import views


app_name = 'catalog_app'

urlpatterns = [
    path(r'', views.catalog_page, name='catalog_page'),
    path(r'(?P<pk>\d+)/', views.hotel_card_page, name='hotel_page'),
]