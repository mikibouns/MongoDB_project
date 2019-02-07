from django.core.management.base import BaseCommand
from catalog_app.models import Hotel
from django.contrib.auth.models import User
from subprocess import call
import os
import shutil
from pprint import pprint
from random import randint
import datetime

db_path = r'D:\Programms\MongoDB\data\db'

try:
    call(r'net stop MongoDB', shell=True)
    shutil.rmtree(db_path)
    print('deleted databases')
    call(r'mkdir {}'.format(db_path), shell=True)
    print('created "db"')
    call(r'net start MongoDB', shell=True)
except Exception as e:
    print(e)

try:
    os.remove(r'catalog_app\migrations\0001_initial.py')
    print('catalog_app migrations deleted ')
    os.remove(r'django\contrib\auth\migrations\0001_initial.py')
    print('Auth migrations deleted ')
except Exception as e:
    print('Migrations is not found!')

for command in ['makemigrations', 'migrate']:
    try:
        call('manage.py {}'.format(command), shell=True)
        print('{} completed successfully'.format(command))
    except Exception as e:
        print(e)


CATEGORY = [
    {'name': 'Junior Suite'},
    {'name': 'Suite'},
    {'name': 'De Luxe'},
    {'name': 'Duplex'},
    {'name': 'Family Room'},
    {'name': 'Studio'},
    {'name': 'Standart'},
    {'name': 'Village'},
    {'name': 'Apartament'},
    {'name': 'Honeymoon Room'}
]

HOTEL = {
    'name': 'The Oberoi Udaivilas',
    'description': 'Комплекс Oberoi находится в городе Удайпур на территории бывших охотничьих угодий потомков махараджей. Потрясающие виды на зелёный сад и озеро Пичола открываются отовсюду. Сам отель похож на замок, пребывание в котором посетители сравнивают с индийской сказкой.',
    'img': r'\hotels\1.jpg',
    'room': {

    }
}

ROOMS = [
    {'number': 1,
     'places': 2,
     'description': 'any room',
     'price': 10000,
     'img': r'\rooms\1_1.jpg'},
    {'number': 2,
     'places': 1,
     'description': 'any room',
     'price': 10000,
     'img': r'\rooms\1_2.jpg'},
    {'number': 3,
     'places': 3,
     'description': 'any room',
     'price': 10000,
     'img': r'\rooms\1_3.jpg'}
]

class Command(BaseCommand):
    def handle(self, *args, **options):

        User.objects.all().delete()
        for user in range(1, 11):
            new_user = User.objects.create_user(
                username='user{}'.format(user),
                email='user{}@mail.com'.format(user),
                password='123',
            )
            new_user.save()

        # Создаем суперпользователя при помощи менеджера модели
        super_user = User.objects.create_superuser('admin', 'admin@mail.com', '123')

        Hotel.objects.mongo_insert_one(HOTEL)

        hotel = Hotel.objects.mongo_find_one({'name': 'The Oberoi Udaivilas'})
        pprint(hotel)

        # Hotel.objects.update({'name': 'The Oberoi Udaivilas'}, {'$push': {'room': ROOMS}})