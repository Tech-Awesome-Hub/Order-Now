from django.db import models

class Vendor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/vendor/')

    #save the data
    def register(self):
        self.save()

    @staticmethod
    def get_all_vendors():
        return Vendor.objects.all()

    @staticmethod
    def get_vendors_by_email(email):
        try:
            return Vendor.objects.get(email=email)
        except:
            return False
    
    def doesExist(self) :
        if Vendor.objects.filter(email=self.email):
            return True
        else:
            return False
    
    def __str__(self):
        return self.company_name