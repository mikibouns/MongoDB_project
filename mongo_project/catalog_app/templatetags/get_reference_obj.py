from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter(name='reference_obj')
@stringfilter
def get_value_by_reference(value):

    pass


# register = template.Library()

