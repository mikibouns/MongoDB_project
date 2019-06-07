from django.urls import path
from . import views

app_name = 'auth_app'

urlpatterns = [
    path(r'login', views.login, name='login'),
    path(r'logout', views.logout, name='logout'),
    path(r'registration', views.registration, name='reg')
]