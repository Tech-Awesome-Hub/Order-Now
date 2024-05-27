from django import template

register = template.Library()

@register.filter(name='currency')
def currency(number):
    return "    GHS "+str(number)

@register.filter(name='multiply')
def multiply(number , number1):
    return number * number1

@register.filter(name='unit_available')
def unit_available(products, filter):
    result = 0
    if len(products) > 0:
        for product in products:
            if product.filter.name == filter.name:
                result += 1
    return result

@register.filter(name='all_unit')
def all_unit(products, filter):
    result = 0
    if len(products) > 0:
        for product in products:
            if product.filter.parent_filter == filter.name:
                result += 1
    return result

@register.filter(name='also_like')
def also_like(products, item):
    result = []
    if len(products) > 0:
        for i in item:
            for product in products:
                if len(result) >= 5:
                    break
                elif product.category == i.category:
                    result.append(product)
    
    return result