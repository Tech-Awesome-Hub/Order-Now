from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from store.models.cart import get_cart
from django.views import View
from .home import store

class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get ('return_url')
        return render (request, 'store/login.html')

    def post(self, request):
        email = request.POST.get ('email')
        password = request.POST.get ('password')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

        customer = None
        if Customer.isExists(email):
            customer = Customer.get_customer_by_email (email)

        error_message = None
        if customer:
            flag = check_password (password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    add_cart(request)
                    return HttpResponseRedirect (Login.return_url)
                else:
                    Login.return_url = None
                    add_cart(request)
                    return store(request)
            else:
                error_message = 'Invalid !!'
        else:
            error_message = 'Invalid !!'

        # print (email, password)
        return render (request, 'store/login.html', {'error': error_message})


def remove_session_parameter(request, parameter_name):
    # Assuming 'parameter_name' is the parameter you want to remove
    if parameter_name in request.session:
        del request.session[parameter_name]
        # Alternatively, you can use pop() method:
        # request.session.pop('parameter_name')


def add_session_parameter(request, parameter_name, parameter_value):
    request.session[parameter_name]=parameter_value

def logout(request):
    request.session.clear()
    error_message = None
    return render (request, 'store/login.html', {'error': error_message})

def add_cart(request):
    if get_cart(request=request) and get_cart(request=request) != None:
        cart = get_cart(request=request)
        request.session['cart'] = cart
    