from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from store.models.sub_category import SubCategory
from django.views import View
from django.urls import reverse

class DetailView(View):

    def post(self , request, product_id):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        add = request.POST.get('add')
        cart = request.session.get('cart')
       
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove == 'True':
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                elif add == 'True':
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return self.get(request, product_id)
    
    def get(self, request, product_id):
        
        cart = request.session.get('cart')
        vendors = request.session.get('vendor')
        product = request.session.get('id')
        

        if not cart:
            request.session['cart'] = {}

        product = None
        
        categories = Category.get_all_categories()
        sub_categories = SubCategory.get_all_sub_categories()

       
        if product_id:
            product = Product.get_products_by_specificid(product_id)
        else:
            product = []

        data = {}
        data['products'] = product
        data['categories'] = categories
        data['sub_categories'] = sub_categories
        data['vendors'] = vendors

        print('you are : ', request.session.get('email'))
        return render(request, 'store/detail.html', data)

