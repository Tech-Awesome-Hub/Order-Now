from django import template

register = template.Library ()

@register.filter (name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys ()
    for id in keys:
        if int (id) == product.id:
            return True
    return False;

@register.filter (name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys ()
    for id in keys:
        if int (id) == product.id:
            return cart.get (id)
    return 0;

@register.filter (name='shipping_cost')
def shipping_cost(product):
    try:
        if not product.shippingcost:
            shipping_cost = int(0)
        else:
            shipping_cost = product.shippingcost
    except:
        shipping_cost = int(0)
    return shipping_cost

@register.filter (name='sub_total')
def sub_total(products, cart):
    sum = 0
    for p in products:
        sum += price_total (p, cart)
        sum += shipping_cost (p)
    return sum
        
@register.filter (name='shipping_total')
def shipping_total(products):
    sum_shipping = 0
    for p in products:
        sum_shipping += shipping_cost (p)
    return sum_shipping

@register.filter (name='price_total')
def price_total(product, cart):
    return product.price * cart_quantity (product, cart)

@register.filter (name='total_cart_price')
def total_cart_price(products, cart):
    sum = 0
    for p in products:
        sum += price_total (p, cart)
        sum += shipping_cost (p)
    return sum
