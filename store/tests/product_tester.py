from django.test import TestCase
from ..models.product import Products


class ProductsModelTest(TestCase):
    def test_get_all_products(self):
        '''
          
        '''
        all_products = Products.get_all_produts()

        self.assertIs(all_products, object)
    