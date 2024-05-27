from django import template

register = template.Library ()

@register.filter (name='is_in_category')
def is_in_category(item, cat):
    if str(item.parent_category) == str(cat.name):
            return item.name
    return ''


@register.filter(name='isavailable')
def isavailable(item):
    return item == ''

@register.filter(name='available_category')
def available_category(item):
    return item