from django.contrib.auth import get_user_model
from django.db import models


class Cart(models.Model):
    """
    Модель корзины покупок для пользователя.

    Корзина связана с пользователем и хранит информацию о дате её создания.
    Пользователь может иметь только одну корзину, и все товары, добавленные в корзину,
    будут храниться в связи с этой моделью.
    """
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Возвращает строковое представление корзины.

        Если корзина связана с пользователем, то строка будет вида:
        "Корзина {id} - {пользователь}".
        Если корзина не связана с пользователем (например, если это анонимная корзина),
        то возвращается строка "Корзина {id}".

        Пример:
        - "Корзина 1 - user123"
        - "Корзина 2"
        """
        return f"Корзина {self.id} - {self.user}" if self.user else f"Корзина {self.id}"


class CartItem(models.Model):
    """
    Модель элемента корзины.

    Каждый элемент корзины представляет товар, который добавлен в корзину, и количество
    этого товара. Связь между корзиной и товаром осуществляется через ForeignKey. Количество товара
    определяется через поле `quantity`, которое по умолчанию равно 1.

    Один товар может быть добавлен в корзину несколько раз, при этом количество товара будет
    увеличиваться.
    """
    cart = models.ForeignKey('Cart', related_name='cart_items', on_delete=models.CASCADE)
    item = models.ForeignKey('item.Item', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        """
        Возвращает строковое представление элемента корзины.

        Строка включает в себя название товара и его количество. Формат строки:
        "{название товара} x{количество}". Например:
        - "Товар 1 x3"
        - "Товар 2 x1"

        Это представление помогает лучше понять, какие товары и в каком количестве
        находятся в корзине.
        """
        return f"{self.item.name} x{self.quantity}"
