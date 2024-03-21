from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from store.models.vendors import Vendor
from store.models.sub_category import SubCategory
from store.models.product_type import ProductType
from django.views import View
 
 
# Create your views here.
class IndexView(View):
 
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
        print('cart@@@@', request.session['cart'])
        return redirect('homepage')
 

    def get(self, request):
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

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
 
def store(request):

    addCart(request)
    cart = request.session.get('cart')

    if not cart:
        request.session['cart'] = {}

    products = None
    categories = Category.get_all_categories()
    types = ProductType.get_all_product_type()
    sub_categories = SubCategory.get_all_sub_categories()
    vendors = Vendor.get_all_vendors()
    categoryID = request.GET.get('category')

    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()

    print(products)

    data = {}
    data['products'] = products
    data['categories'] = categories
    data['vendors'] = vendors
    data['sub_categories'] = sub_categories
    data['types'] = types

    print('you are : ', request.session.get('email'))
    return render(request, 'store/index.html', data)