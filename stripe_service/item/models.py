from django.db import models


class Item(models.Model):
    """
    Модель для представления товаров.
    """

    class Currency(models.TextChoices):
        """
        Перечисление доступных валют.
        """
        USD = 'usd', 'Доллар США'
        RUB = 'rub', 'Российский рубль'
        EUR = 'eur', 'Евро'

    name = models.CharField(
        max_length=255,
        verbose_name="Название товара"
    )
    description = models.TextField(
        verbose_name="Описание товара"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена товара"
    )
    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.RUB,
        verbose_name="Валюта"
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f"{self.name} — {self.price} {self.currency}"
