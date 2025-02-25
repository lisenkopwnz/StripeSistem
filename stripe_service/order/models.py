from django.core.exceptions import ValidationError
from django.db import models


class Order(models.Model):
    """
    Модель заказа.
    Содержит список товаров, применяемые налоги, скидки и итоговую стоимость.
    """
    items = models.ManyToManyField(
        'item.Item',
        through='OrderItem',
        related_name='orders',
        verbose_name="Товары в заказе"
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Общая стоимость заказа",

    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    taxes = models.ManyToManyField(
        'Tax',
        related_name='orders',
        blank=True,
        verbose_name="Применяемые налоги"
    )
    discounts = models.ManyToManyField(
        'Discount',
        related_name='orders',
        blank=True,
        verbose_name="Применяемые скидки"
    )

    def __str__(self):
        return f"Заказ {self.pk} - {self.total_price}"

    def recalculate_total_price(self):
        """
        Пересчитывает итоговую стоимость заказа.
        """
        total_summ = sum(item.price for item in self.items.all())

        for tax in self.taxes.all():
            total_summ += total_summ * tax.rate / 100

        for discount in self.discounts.all():
            if discount.is_percentage:
                total_summ -= total_summ * discount.value / 100
            else:
                total_summ -= discount.value

        self.total_price = round(total_summ, 2)


class OrderItem(models.Model):
    """
    Промежуточная модель для связи заказов и товаров с количеством.
    """
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    item = models.ForeignKey('item.Item', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")

    def __str__(self):
        return f"{self.quantity} x {self.item.name}"

    class Meta:
        unique_together = ('order', 'item')


class Tax(models.Model):
    """
    Модель налога.
    Позволяет задавать различные налоговые ставки и прикреплять их к заказу.
    """
    name = models.CharField(
        max_length=255,
        verbose_name="Название налога"
    )
    rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Ставка налога (например 20%)"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание налога"
    )

    def __str__(self):
        return f"{self.name} - {self.rate * 100:.2f}%"


class Discount(models.Model):
    """
    Модель скидки.
    Поддерживает как процентные, так и фиксированные скидки.
    """
    code = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Код скидки"
    )
    value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Значение скидки"
    )
    is_percentage = models.BooleanField(
        default=True,
        verbose_name="Является ли скидка процентной"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание скидки"
    )

    def __str__(self):
        return f"{self.code} - {'%' if self.is_percentage else 'Fixed'} {self.value}"

    def clean(self):
        """
        Метод для проверки правильности введенных данных.
        """
        if self.is_percentage:
            if self.value < 0 or self.value > 100:
                raise ValidationError("Процентная скидка должна быть в диапазоне от 0 до 100.")
        else:
            if self.value < 0:
                raise ValidationError("Размер фиксированной скидки не может быть отрицательным.")
