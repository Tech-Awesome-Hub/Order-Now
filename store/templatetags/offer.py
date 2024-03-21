from django import template
from ..models.offer import Offer

register = template.Library ()

@register.filter (name='is_in_category')
def is_in_category(item, cat):
    if str(item.parent_category) == str(cat.name):
            return item.name
    return ''
