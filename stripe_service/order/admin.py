from django.contrib import admin

from order.models import Order, Tax, Discount, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    list_display = ('item', 'quantity')
    ordering = ('item',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_price', 'created_at')
    filter_horizontal = ('taxes', 'discounts')
    inlines = [OrderItemInline]
    search_fields = ('id',)
    ordering = ('-created_at',)
    exclude = ('total_price',)


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate', 'description_short')
    search_fields = ('name',)
    ordering = ('rate',)

    def description_short(self, obj):
        return obj.description[:50] + "..." if obj.description and len(obj.description) > 50 else obj.description

    description_short.short_description = "Краткое описание"


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ("code", "value", "is_percentage", "description_short")
    list_filter = ("is_percentage",)
    search_fields = ("code", "description")
    ordering = ("value",)
    list_editable = ("value", "is_percentage")
    list_per_page = 20

    def description_short(self, obj):
        return obj.description[:50] + "..." if obj.description and len(obj.description) > 50 else obj.description

    description_short.short_description = "Краткое описание"
