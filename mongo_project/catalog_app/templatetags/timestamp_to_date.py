from django import template
import datetime


register = template.Library()


@register.filter(name='timestamp_to_date')
def timestamp_to_date(value, arg):
    normal_date = datetime.datetime.utcfromtimestamp(int(value))
    normal_date = normal_date.strftime(arg)
    return normal_date