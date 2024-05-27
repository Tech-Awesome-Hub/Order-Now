from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField (max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    #to save the data
    def register(self):
        self.save()

    #to save the data
    def update(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        return Customer.objects.get(email = email)
    
    @staticmethod
    def get_customer_by_id(ids):
        return Customer.objects.get(id=ids)
    
    @staticmethod
    def isExists(email):
        if Customer.objects.filter(email = email):
            return True
        return False
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'