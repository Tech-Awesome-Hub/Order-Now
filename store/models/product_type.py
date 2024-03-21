from django.db import models

class ProductType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50, default='some text..')

    @staticmethod
    def get_all_product_type():
        return ProductType.objects.all()

    def doesExist(self) :
        if ProductType.objects.filter(name=self.name):
            return True
        else:
            return False
    
    def __str__(self):
        return self.name