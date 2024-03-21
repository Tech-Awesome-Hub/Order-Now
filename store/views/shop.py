from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from store.models.sub_category import SubCategory
from store.models.filters import FilterUpdate
from django.views import View
from django.urls import reverse
import json

class ShopView(View):
    
    def post(self, request):
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
 
        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return json.dumps([{'status': 'successful'}])
        # return redirect('shop')
    
    def get(self , request):
        return HttpResponseRedirect(reverse(f'/shop{request.get_full_path()[1:]}'))

def addCart(request):

    product = request.POST.get('product')
    remove = request.POST.get('remove')
    add = request.POST.get('add')
    cart = request.session.get('cart')
    
    print(cart, product)
    if product:
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
        return json.dumps([{'status': 'successful'}])
        # return redirect('shop')


def remove_session_parameter(request, parameter_name):
    # Assuming 'parameter_name' is the parameter you want to remove
    if parameter_name in request.session:
        del request.session[parameter_name]
        # Alternatively, you can use pop() method:
        # request.session.pop('parameter_name')


def shop(request):
    
    addCart(request)

    cart = request.session.get('cart')
    vendors = request.session.get('vendor')
    
    if not cart:
        request.session['cart'] = {}

    product = None
    query = request.session.get('search_query')
    master_query = request.session.get('search__query')
    
    categories = Category.get_all_categories()
    sub_categories = SubCategory.get_all_sub_categories()
    # filters = FilterUpdate.get

    categoryID = request.GET.get('category')
    sub_categoryID = request.GET.get('sub_category')
    itype = request.GET.get('type')

    found = False

    if query:
        product = Product.get_products_by_name(name=query)
        found = True
    elif master_query:
        product = Product.get_products_by_name(name=master_query)
        found = True
    else:
        if categoryID and type(categoryID) != int:
            product = Product.get_all_products_by_categoryid(categoryID) 
            found = True
        else:
            product = Product.get_all_products_by_type(type=categoryID)
            found = True
        if sub_categoryID:
            product = Product.get_all_products_by_sub_categoryid(sub_categoryID)
            found = True
        if itype:
            product = Product.get_all_products_by_type(type=itype)
            found = True

        if not found:
            product = Product.get_all_products() 

    data = {}
    data['products'] = product
    data['categories'] = categories
    data['sub_categories'] = sub_categories
    data['vendors'] = vendors

    print('you are : ', request.session.get('customer'))
    # print(len(product), categoryID, product)
    
    remove_session_parameter(request,'search_query')
    remove_session_parameter(request,'search__query')

    return render(request, 'store/shop.html', data)

