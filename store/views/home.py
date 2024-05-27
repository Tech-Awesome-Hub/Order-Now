from django.shortcuts import render, HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from store.models.vendors import Vendor
from store.models.sub_category import SubCategory
from store.models.product_type import ProductType
from store.models.offer import Offer
from store.models.cart import add_to_cart, update_cart
from django.views import View
 
 
# Create your views here.
class IndexView(View):

    def get(self, request):
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def addCart(request):
        
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
    offers = Offer.get_all_offers()
    categoryID = request.GET.get('category')

    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories
    data['vendors'] = vendors
    data['sub_categories'] = sub_categories
    data['types'] = types
    data['offers'] = offers

    print('you are : ', request.session.get('email'))
    return render(request, 'store/index.html', data)