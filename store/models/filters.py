# models.py
from django.db import models

class Filter(models.Model):
    name = models.CharField(max_length=50)
    
    @property
    def sub_filter(self):
        try:
            result = []
            filters = self.filters.all()
            if len(filters) > 0:
                for filter in filters:
                    result.append(filter)
            else:
                result=[]
        except:
            result = []

        return []
    
    @staticmethod
    def get_all_filters():
        return Filter.objects.all()
    
    def __str__(self):
        return self.name
    
class FilterUpdate(models.Model):
    name = models.CharField(max_length=50)
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE, default='', related_name='filters')
    
    @property
    def parent_filter(self):
        return self.filter.name
   
    @staticmethod
    def get_all_filters():
        return FilterUpdate.objects.all()
    
    def __str__(self):
        return self.name