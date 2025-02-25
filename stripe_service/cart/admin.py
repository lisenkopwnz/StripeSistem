from django.contrib import admin
from .models import Cart, CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """
    Класс админки для модели Cart.
    """
    list_display = ('id', 'user', 'created_at')
    search_fields = ('user__username',)
    list_filter = ('created_at',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    """
    Класс админки для модели CartItem.
    """
    list_display = ('cart', 'item', 'quantity')
    list_filter = ('cart', 'item')
    search_fields = ('item__name',)