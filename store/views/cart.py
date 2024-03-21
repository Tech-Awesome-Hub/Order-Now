from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import Product

class Cart(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        destroy = request.POST.get('destroy')
        add = request.POST.get('add')
        cart = request.session.get('cart')
        print(cart, '$$$$$$$$$$$$$$$$$$$$$$', product)
       
        if cart:
            quantity = cart.get(product)

            if quantity:
                if remove == 'True':
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1

                elif destroy == 'True':
                    if quantity>=1:
                        cart.pop(product)
                        product = 0
                   
                elif add == 'True':
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        # else:
        #     cart = {}
        #     cart[product] = 1

        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return self.get(request)
    
    def get(self , request):
        print('@@@@@@@@@@@@@@@@@@@@@@@@@')
        ids = list(request.session.get('cart').keys())
        print(ids,'@@@@@@@@@@@@@@@@@@@@@@@@@')
        products = Product.get_products_by_id(ids)
        print(products, '@@@@@@@@@@@@@@@@@@@@@@@@@')
        return render(request , 'store/cart.html' , {'products' : products} )

