from django.db import models


class OrderPayment(models.Model):
    """
    Модель оплаты заказа.
    Хранит информацию о статусе платежа и идентификатор сессии Stripe.
    """

    order = models.ForeignKey(
        'order.Order',
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name="Заказ"
    )
    stripe_session_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Идентификатор сессии Stripe"
    )
    is_paid = models.BooleanField(
        default=False,
        verbose_name="Статус оплаты заказа"
    )

    class Meta:
        verbose_name = "Оплата заказа"
        verbose_name_plural = "Оплаты заказов"

    def __str__(self):
        return f"Оплата заказа {self.order.id} - {'Оплачено' if self.is_paid else 'Ожидает оплаты'}"
