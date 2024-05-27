from django.shortcuts import render
from store.models.product import Product
from store.models.category import Category
from store.models.sub_category import SubCategory
from store.models.customer import Customer
from store.models.cart import add_to_cart, update_cart
from django.views import View

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from store.serializers import ProductSerializer
from store.serializers import CategorySerializer
from store.serializers import SubCategoryProductSerializer

class DetailView(View):

    def post(self , request, product_id):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        add = request.POST.get('add')
        cart = request.session.get('cart')
       
        if product:
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
                    elif add == 'True':
                        cart[product]  = quantity+1
                        update_cart(request=request, cart=cart)

                else:
                    cart[product] = 1
                    update_cart(request=request, cart=cart)
            else:
                cart = {}
                cart[product] = 1
                add_to_cart(request=request, cart=cart)
        
        request.session['cart'] = cart
        return self.get(request, product_id, state=1)
    
    def get(self, request, product_id, state=0):
        
        cart = request.session.get('cart')
        vendors = request.session.get('vendor')

        if not cart:
            request.session['cart'] = {}

        product = None
        
        categories = Category.get_all_categories()
        sub_categories = SubCategory.get_all_sub_categories()

        try:
            customer = Customer.get_customer_by_id(ids=request.session.get('customer'))
            customer = f'{customer.first_name} {customer.last_name}'
        except:
            customer = ''

        if product_id:
            product = Product.get_products_by_specificid(product_id)
        else:
            product = []
        
        if state == 0:
            data = {}
            data['products'] = product
            data['categories'] = categories
            data['sub_categories'] = sub_categories
            data['vendors'] = vendors
            data['customer'] = customer
            data['all_products'] = Product.get_all_products()

            print('you are : ', request.session.get('customer'))
            return render(request, 'store/detail.html', data)
        else:
            data = {
                'quantity': cart_quantity(product_id, cart),
                'len': len(cart.keys())
            }
            return JsonResponse(data, safe=False)

def cart_quantity(product_id, cart):
    keys = cart.keys ()
    for id in keys:
        if int (id) == product_id:
            return cart.get (id)
    return 0;
    # data = {}
    #     data['products'] = ProductSerializer(product, many=True).data
    #     data['categories'] = CategorySerializer(categories, many=True).data
    #     data['sub_categories'] = SubCategoryProductSerializer(sub_categories, many=True).data
    #     data['vendors'] = vendors
    #     data['customer'] = customer
    #     data['all_products'] = ProductSerializer(Product.get_all_products(), many=True).data

    #     print('you are : ', request.session.get('customer'))
    #     return JsonResponse(data, safe=False)

