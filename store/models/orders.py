from django.db import models
from .product import Product
from .customer import Customer
from .vendors import Vendor
import datetime


class Order(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField (max_length=50, default='', blank=True)
    phone = models.CharField (max_length=50, default='', blank=True)
    date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE,default=1 )

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
    
    @staticmethod
    def get_all_products_by_vendorid(vendor_id):
        if vendor_id:
            return Vendor.objects.filter (vendor=vendor_id)
        else:
            return Vendor.get_all_products();

