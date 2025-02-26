from django.urls import path

from cart import views
from cart.views import CartList, AddToCart

app_name = 'cart'

urlpatterns = [
    path('', CartList.as_view(), name='cart_list'),
    path('add-to-cart/', AddToCart.as_view(), name='add_to_cart'),
]