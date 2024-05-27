from django.db import models
from .customer import Customer

class ShippingLocations(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    full_name = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=10, default='')
    address_line1 = models.CharField(max_length=50, default='')
    address_line2 = models.CharField(max_length=50, default='')
    shipping_area = models.CharField(max_length=100, default='')
   
    def saveAddr(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return ShippingLocations.objects.filter(customer=customer_id)
    
    @staticmethod
    def get_location_by_id(ids):
        return ShippingLocations.objects.filter (id__in=ids)
    
    @staticmethod
    def get_all_locations():
        return ShippingLocations.objects.all()
