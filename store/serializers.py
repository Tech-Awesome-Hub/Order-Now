from rest_framework import serializers
from store.models.product import Product
from store.models.category import Category
from store.models.sub_category import SubCategory

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'
