from django.urls import path, re_path
from . import views


app_name = 'catalog_app'

urlpatterns = [
    path('', views.catalog_page, name='catalog_page'),
    path(r'<str:short_name>/', views.hotel_page, name='hotel_page'),
]