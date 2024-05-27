from django.db import models
from .category import Category

class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    parent_category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
    image = models.ImageField(upload_to=f'uploads/sub_category/', default='')
    
    @staticmethod
    def get__sub_category_by_id(ids):
        return SubCategory.objects.filter (id__in=ids)
    
    @staticmethod
    def get_all_sub_categories():
        return SubCategory.objects.all()

    @staticmethod
    def get_all_sub_category_by_categoryid(category_id):
        if category_id:
            return SubCategory.objects.filter (category=category_id)
        else:
            return SubCategory.get_all_sub_categories();

    def __str__(self):
        return self.name
