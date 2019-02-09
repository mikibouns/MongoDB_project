from django.core.management.base import BaseCommand
from catalog_app.models import Hotel, Category, ReservedDate
from django.contrib.auth.models import User
from subprocess import call
import os
import shutil
from pprint import pprint
from random import randint, choice
import datetime
import time


# db_path = r'D:\Programms\MongoDB\data\db'
#
# try:
#     call(r'net stop MongoDB', shell=True)
#     shutil.rmtree(db_path)
#     print('deleted databases')
#     call(r'mkdir {}'.format(db_path), shell=True)
#     print('created "db"')
#     call(r'net start MongoDB', shell=True)
# except Exception as e:
#     print(e)

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

category_list = [i['name'] for i in CATEGORY]


def add_reserved():
    reversed_list = []
    users = ['user{}'.format(i) for i in range(1, 11)]
    for _ in range(8):
        person = User.objects.get(username=choice(users))
        start_date = datetime.date(randint(2019, 2019), randint(1, 2), randint(1, 28))
        last_date = start_date + datetime.timedelta(randint(1, 30))
        reserved_data = {
            'person': person.id,
            'check_in': time.mktime(start_date.timetuple()),
            'check_out': time.mktime(last_date.timetuple())
        }
        reversed_list.append(reserved_data)
    return reversed_list


def add_hotels():
    hotels = []
    jpg_count = 1
    hotels_dict = {'The Oberoi Udaivilas': 'Комплекс Oberoi находится в городе Удайпур на территории бывших охотничьих \
                    угодий потомков махараджей. Потрясающие виды на зелёный сад и озеро Пичола открываются отовсюду. \
                    Сам отель похож на замок, пребывание в котором посетители сравнивают с индийской сказкой.',
                   'Baros Maldives': 'Этот титул отель получает уже в пятый раз. Главное отличие Baros Maldives в том,\
                    что он только для взрослых. Детей младше 8 лет здесь не принимают, ведь это место создано для отдыха в тишине.',
                   'Armani Hotel Dubai': 'Неповторимый дизайн отеля разработал знаменитый модельер Джорджио Армани. \
                   Номера занимают 11 этажей небоскрёба в самом сердце Дубая. В знаменитый торговый центр Dubai Mall \
                   можно попасть прямо из лифта отеля. Из окон открывается панорамный вид на город и поющие фонтаны.',
                   'Mriya Resort & Spa': 'У отеля есть собственный пляж, дорога до которого занимает всего 5 минут. \
                   К услугам гостей Mriya Resort & Spa 9 баров и ресторанов и ночной клуб. Любителям водных процедур \
                   придутся по вкусу крытый и открытый бассейны, спа-центр, сауна, хаммам и джакузи. Здесь можно \
                   заняться теннисом, сквошем или поиграть в боулинг. В отеле действует бесплатный кинотеатр.',
                   'Dukes London': 'Отреставрированный исторический отель Dukes расположен в районе Мейфейр в \
                   Вестминстере. Самые интересные музеи, дворцы и брендовые магазины находятся совсем близко. Отель \
                   Dukes — это английская классика, дополненная современными удобствами. А вот мраморная баня здесь выполнена в итальянском стиле.',
                   'Peninsula': 'Отель находится в Париже, совсем рядом с Триумфальной аркой. В первую очередь Peninsula\
                    — это роскошь и элегантность. Номера и холлы просторные, с высокими потолками и непременно украшены\
                     произведениями искусства. Многие считают Peninsula лучшим европейским отелем.',
                   'Finch Bay Galapagos Hotel': 'Это уютный небольшой отель, который подойдёт любителям экзотической \
                   флоры и фауны. Здесь нет шумного веселья по вечерам, но это компенсируется живописными видами и \
                   обилием экскурсий. В некоторых номерах есть балконы с гамаками. Finch Bay Galapagos Hotel — прекрасное место для отдыха в тишине.',
                   'The Venetian Macao Resort Hotel': 'The Venetian Macao — 39-этажный небоскрёб, седьмое по величине \
                   здание в мире, построенное в центре города. Вряд ли это хороший вариант для отдыха с детьми, зато \
                   взрослые здесь развлекаются от души. Это не только отель, но и огромное казино, развлекательная арена\
                    на 15 000 человек, множество выставочных и конференц-залов.',
                   'San Clemente Palace Kempinski Venice': 'Kempinski — известнейшая сеть пятизвёздочных отелей, которой\
                    вот уже более ста лет. Отель San Clemente Palace находится в Венеции на собственном острове. \
                    На этом месте раньше был расположен монастырь, от которого осталась часовня XII века. По \
                    договорённости в ней проводят обряды венчания. Большую часть острова занимает парк, в котором \
                    посетители отеля могут загорать, бегать по дорожкам или пить коктейли у прудов.',
                   'Angel’s Marmaris': 'Отель Angel’s Marmaris — это релаксация и забота о здоровье. К услугам гостей \
                   есть турецкая и паровая бани, сауна, джакузи и чудодейственная солевая комната. Особенностью отеля, \
                   помимо отсутствия алкоголя, является наличие отдельных бассейнов и пляжей только для женщин или \
                   мужчин. В таких условиях каждый почувствует себя комфортно.'}
    for name, desc in hotels_dict.items():
        hotel = {
            'name': name,
            'description': desc,
            'img': r'\hotels\{}.jpg'.format(jpg_count),
            'room': []
        }
        hotels.append(hotel)
        jpg_count += 1
    return hotels


def add_rooms():
    room_list = []
    for i in range(1, 6):
        room_dict = {
            'category': Category.objects.mongo_find_one({'name': choice(category_list)})['_id'],
            'number': i,
            'places': randint(1, 5),
            'description': 'any description',
            'price': randint(5000, 50000),
            'img': '',
            'reserved': []
        }
        room_list.append(room_dict)
    return room_list


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

        for category in CATEGORY:
            new_category = Category(**category)
            new_category.save()

        Hotel.objects.mongo_insert_many(add_hotels())

        for hotel in Hotel.objects.mongo_find():
            Hotel.objects.mongo_update_many(hotel, {'$set': {'room': add_rooms()}})

        for hotel in Hotel.objects.mongo_find():
            Hotel.objects.mongo_update(
                hotel,
                {'$push': {'room.$[].reserved': {'$each': add_reserved()}}},
            )

#-----------------------------------------------------------------------------------------------------------------------


        # for hotel in Hotel.objects.mongo_find({}, {'_id': 0, 'name': 1}):
        #     pprint(hotel['name'])
        #
        # for hotel in Hotel.objects.all():
        #     pprint(hotel.img)

        # hotel = Hotel.objects.mongo_find()
        # pprint(hotel.objects.mongo_find_one({'name': 'The Oberoi Udaivilas'}))

        # for hotel in Hotel.objects.mongo_find():
        #     Hotel.objects.mongo_find_one(hotel, {'$set': {'room': {'reserved': add_reserved()}}})
        #     pprint('OK')

        # pprint(Hotel.objects.mongo_find_one({'name': 'The Oberoi Udaivilas'})['room'][0]['reserved'])

        # Hotel.objects.mongo_update({'name': 'Mriya Resort & Spa'}, {'_id': 0, 'room': {'$elemMatch': {'number': 2}}})
        # pprint(room)





