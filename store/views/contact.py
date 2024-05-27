from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from django.urls import reverse

class Contact(View):
   
    def get(self, request):
        # return HttpResponseRedirect(reverse(f'/login{request.get_full_path()[1:]}'))
        return render( request, 'store/contact.html')
    
    def post(self, request):
        email = request.Get.get('email')
        customer = Customer.get_customer_by_email(email)
        return render (request, 'contact.html', {'customer': customer, 'email': email})

