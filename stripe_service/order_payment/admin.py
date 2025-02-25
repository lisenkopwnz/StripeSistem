from django.contrib import admin

from order_payment.models import OrderPayment


@admin.register(OrderPayment)
class OrderPaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'stripe_session_id', 'is_paid', 'payment_status')
    list_filter = ('is_paid',)
    search_fields = ('order__id', 'stripe_session_id')
    ordering = ('-order__created_at',)
    list_per_page = 20

    def payment_status(self, obj):
        return 'Оплачено' if obj.is_paid else 'Ожидает оплаты'

    payment_status.short_description = 'Статус оплаты'

    def has_add_permission(self, request, obj=None):
        """
        Отключить возможность добавлять новые оплаты вручную.
        """
        return False

    def has_delete_permission(self, request, obj=None):
        """
        Отключить возможность удалять оплаты вручную.
        """
        return False  # Не разрешаем удалять оплаты вручную
