from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order
from store.models.customer import Customer
from store.models.shipping_loc import ShippingLocations

class CheckOut(View):
    def post(self, request):
        address1 = request.POST.get('address-line1')
        address2 = request.POST.get('address-line2')
        phone = request.POST.get('phone')
        full_name = request.POST.get('full-name')
        shipping_area = request.POST.get('shippin-area')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address1, address2, phone, customer, cart, products, request.POST.get("save_address"))
        pay = None
        

        if pay:
            for product in products:
                print(cart.get(str(product.id)))
                order = Order(customer=Customer(id=customer),
                            product=product,
                            price=product.price,
                            address=shipping_area,
                            phone=phone,
                            quantity=cart.get(str(product.id)))
                order.save()
            
            if request.POST.get("save_address"):
                try:
                    c = ShippingLocations(id=customer)
                    if check_address(address1, address2, c):
                        c.address_line1 = address1
                        c.address_line2 = address2
                        c.full_name = full_name
                        c.shipping_area = shipping_area
                        c.customer = customer
                        c.phone = phone
                        c.saveAddr()
                    else:
                        print("address exits")
                except:
                    pass

            request.session['cart'] = {}
            url = 'store/cart.html'
            context = {}
        else:
            c = Customer(id=customer)
            url = 'store/checkout.html'
            context = {
                        'address-1':address1,
                        'address-2':address2,
                        'phone':phone,
                        'save_address': request.POST.get("save_address")
                    }

        return render (request, url, context)

def check_address(addr1, addr2, c):
    status = False
    if c.address_line1 == '':
        status = True
    elif c.address_line2 == '':
        status = True
    elif c.address_line2 == '':
        status = True

    return status
