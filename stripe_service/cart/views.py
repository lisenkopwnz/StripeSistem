from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from cart.models import Cart, CartItem
from item.models import Item


class CartList(LoginRequiredMixin, ListView):
    template_name = 'cart/cart_list.html'
    context_object_name = 'cart_list'

    def get_login_url(self):
        return reverse('user:login')

    def get_queryset(self):
        # Получаем текущего пользователя
        user = self.request.user
        # Пытаемся получить корзину для пользователя
        try:
            cart = Cart.objects.get(user=user)# Если корзина не найдена, выбрасывается Cart.DoesNotExist
        except Cart.DoesNotExist:
            raise Http404("Корзина не найдена для этого пользователя.")  # Возвращаем 404, если корзина не найдена

        # Получаем все элементы корзины
        cart_list = CartItem.objects.filter(cart=cart)

        return cart_list

class AddToCart(View):

    def post(self, request):
        item_id = request.POST.get('item_id')

        user = request.user

        item = Item.objects.get(pk=item_id)
        cart = Cart.objects.get(user=user)

        cart_item = CartItem.objects.create(item=item,cart=cart)

        cart_item.save()
        return JsonResponse({'status': 'success', 'message': 'Товар добавлен в корзину!'})
