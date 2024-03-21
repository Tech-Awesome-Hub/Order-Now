from django.db import models
from .category import Category
from .sub_category import SubCategory
from .product_type import ProductType
from .vendors import Vendor
from .filters import Filter, FilterUpdate


class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    unit_available = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default='' ) 
    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE, default='' , null=True, blank=True) 
    type = models.ForeignKey(ProductType,on_delete=models.CASCADE, default='' , null=True, blank=True)
    filter = models.ForeignKey(FilterUpdate,on_delete=models.CASCADE,default='', null=True, blank=True )
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE,default='', null=True, blank=True )
    description = models.TextField(max_length=1000, default='some text')
   
    @property
    def image_url(self):
        try:
            result = []
            photos = self.photos
            if len(photos) > 0:
                for photo in photos:
                    result.append(photo.url)
            else:
                result = ['uploads/placeholder.png']

        except:
            result = ['uploads/placeholder.png']
        return result
    
    @staticmethod
    def get_products_by_specificid(ids):
        try :
            return Product.objects.filter (id=ids)
        except:
            print('error found')
            
    @staticmethod
    def get_products_by_name(name):
        return Product.objects.filter(name__icontains=name)    
      
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter (id__in=ids)
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter (category=category_id)
        else:
            return Product.get_all_products()
        
    @staticmethod
    def get_all_products_by_type(type):
        try:
            return Product.objects.filter(type=type)
        except:
            return False
         
    def get_all_products_by_sub_categoryid(sub_category_id):
            if sub_category_id:
                return Product.objects.filter(sub_category=sub_category_id)
            else:
                return Product.get_all_products()

    @staticmethod
    def get_all_products_by_vendorid(vendor_id):
        if vendor_id:
            return Product.objects.filter (vendor=vendor_id)
        else:
            return Product.get_all_products()
    
    @staticmethod
    def get_all_products_by_type(type):
        if type:
            return Product.objects.filter (type=type)
        else:
            return Product.get_all_products()
    
    def __str__(self):
        return self.name
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,default='', related_name='photos')
    photo = models.ImageField(upload_to='uploads/product')

    def __str__(self):
        return self.product.name