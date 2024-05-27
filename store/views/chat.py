from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from django.urls import reverse

class Chat(View):
   
    def get(self, request):
        # return HttpResponseRedirect(reverse(f'/login{request.get_full_path()[1:]}'))
        return render( request, 'store/chat.html')
    
    def post(self, request):
        email = request.Get.get('email')
        customer = Customer.get_customer_by_email(email)
        return render (request, 'chat.html', {'customer': customer})

def endchat(request):
    request.session.clear()
    return redirect('homepage')
