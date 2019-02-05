from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path(r'', views.main_page, name='main_page'),
]