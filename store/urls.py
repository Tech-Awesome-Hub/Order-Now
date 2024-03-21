from django.urls import path
from .views.home import IndexView, store
from .views.cart import Cart
from .views.shop import ShopView, shop
from .views.login import Login, logout
from .views.signup import Signup
from .views.chat import Chat
from .views.contact import Contact
from .views.detail import DetailView
# from .views.checkout import CheckOut
# from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from .views.search import search_view
from .views.filter import filter_view

app_name = 'store' 
urlpatterns = [
    path("", IndexView.as_view(), name="homepage"),
    path('store', store , name='store'),
    path("", ShopView.as_view(), name="shoppingmall"),
    path('shop', shop , name='shop'),
    path('login', Login.as_view(), name='login'),
    path('signup', Signup.as_view(), name='signup'),
    path('logout', logout , name='logout'),
    path('chat', Chat.as_view(), name='chat'),
    path('contact', Contact.as_view(), name='contact'),
    path('detail#<int:product_id>', DetailView.as_view(), name='detail'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('search/', search_view, name='search_view'),
    path('filter/', filter_view, name='filter_view')
    # path('check-out', CheckOut.as_view() , name='checkout'),
    # path('orders', auth_middleware(OrderView.as_view()), name='orders'),
] 