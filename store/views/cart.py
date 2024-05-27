from django.shortcuts import render
from django.views import  View
from store.models.product import Product
from store.models.customer import Customer
from store.models.shipping_loc import ShippingLocations
from store.models.cart import get_cart, update_cart, add_to_cart

class Cart(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        destroy = request.POST.get('destroy')
        add = request.POST.get('add')
        cart = request.session.get('cart')
       
        if cart:
            quantity = cart.get(product)

            if quantity:
                if remove == 'True':
                    if quantity<=1:
                        cart.pop(product)
                        update_cart(request=request, cart=cart)
                    else:
                        cart[product]  = quantity-1
                        update_cart(request=request, cart=cart)

                elif destroy == 'True':
                    if quantity>=1:
                        cart.pop(product)
                        product = 0
                        update_cart(request=request, cart=cart)
                   
                elif add == 'True':
                    cart[product]  = quantity+1
                    update_cart(request, cart)

            else:
                cart[product] = 1
                update_cart(request, cart)
        
        request.session['cart'] = cart
        return self.get(request)
    
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        locations = ShippingLocations.get_all_locations()
        customer = Customer.get_customer_by_id(ids=request.session.get('customer'))
        
        if customer:
            phone = customer.phone
        else: 
            phone = ''

        if len(ids) > 0:
            if not get_cart(request=request) and get_cart(request=request) == None:
                add_to_cart(request=request, cart=request.session['cart'])
    
        return render(request , 'store/cart.html' , {
            'products' : products,
            'locations' : locations,
            'phone' : phone
        } )

