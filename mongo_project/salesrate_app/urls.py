from django.urls import path
from . import views

app_name = 'salesrate_app'

urlpatterns = [
    path(r'', views.sales_rate_page, name='sales_rate_page'),
]