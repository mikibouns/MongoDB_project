from django import template
from ..models import Category

register = template.Library()


@register.filter(name='dbref_data')
def get_dbref_data(value, arg):
    obj = Category.objects.mongo_find_one({'_id': value.id})
    return obj[arg]

