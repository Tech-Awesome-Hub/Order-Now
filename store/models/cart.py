from django.conf import settings
from django.shortcuts import get_object_or_404
from django.db import models
import json

class CartItem(models.Model):
    user = models.AutoField(primary_key=True)
    data = models.JSONField()
    # price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.user}'

def add_to_cart(request, cart):

    if request.session.get('customer'):
        # Serialize the dictionary to JSON
        serialized_data = json.dumps(cart)

        # Create an instance of the model and set the serialized data
        cart_item = CartItem(user=request.session.get('customer'), data=serialized_data)

        # Save the cart item to the database
        cart_item.save()

def remove_from_cart(request):

    if request.session.get('customer'):
        # Retrieve the cart items associated with the session
        cart_items = CartItem.objects.filter(user=request.session.get('customer'))

        # Delete the cart items
        cart_items.delete()


def destroy_cart(request):

    if request.session.get('customer'):
        # Retrieve the cart items associated with the session
        cart_items = CartItem.objects.get(user=request.session.get('customer'))

        # Delete the cart items
        cart_items.delete()


def update_cart(request, cart):

    if request.session.get('customer'):
        cart_item = get_object_or_404(CartItem, user=request.session.get('customer'))
        serialized_data = json.dumps(cart)
        cart_item.data = serialized_data
        cart_item.save()


def get_cart(request):

    if request.session.get('customer'):
        try:
            cart_item = CartItem.objects.get(user=request.session.get('customer'))
            data = json.loads(cart_item.data)
        except :
            data = None
        return data        
        