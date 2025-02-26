from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from cart.models import Cart


@receiver(post_save, sender=get_user_model())
def create_cart_for_new_user(sender, instance, created, **kwargs):
    """
    Сигнал для автоматического создания корзины при регистрации нового пользователя.
    """
    if created:
        # Создаем корзину для нового пользователя
        Cart.objects.create(user=instance)