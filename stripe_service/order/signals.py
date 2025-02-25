from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

from order.models import OrderItem, Order


@receiver(post_save, sender=OrderItem)
def order_item_added(sender, instance, created, **kwargs):
    """
    Сигнал, срабатывающий после создания или обновления OrderItem.
    Пересчитывает общую стоимость заказа, к которому добавлен/обновлен товар.
    """
    order = instance.order  # Получаем заказ, к которому относится этот товар
    order.recalculate_total_price()  # Пересчитываем общую стоимость
    order.save()  # Сохраняем заказ с обновленной стоимостью

@receiver(m2m_changed, sender=Order.taxes.through)
def order_taxes_changed(sender, instance, action, **kwargs):
    """
    Сигнал, срабатывающий при изменении связи заказа с налогами (добавление/удаление налогов).
    Пересчитывает общую стоимость заказа при изменении налогов.
    """
    if action in ['post_add', 'post_remove']:
        instance.recalculate_total_price()  # Пересчитываем стоимость заказа
        instance.save()  # Сохраняем изменения в заказе

@receiver(m2m_changed, sender=Order.discounts.through)
def order_discounts_changed(sender, instance, action, **kwargs):
    """
    Сигнал, срабатывающий при изменении связи заказа с скидками (добавление/удаление скидок).
    Пересчитывает общую стоимость заказа при изменении скидок.
    """
    if action in ['post_add', 'post_remove']:
        instance.recalculate_total_price()  # Пересчитываем стоимость заказа
        instance.save()  # Сохраняем изменения в заказе