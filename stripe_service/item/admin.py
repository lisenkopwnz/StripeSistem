from django.contrib import admin
from item.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "currency", "description_short")  # Отображаемые поля
    list_filter = ("currency",)
    search_fields = ("name", "description")
    ordering = ("price",)
    list_editable = ("price", "currency")
    list_per_page = 20

    def description_short(self, obj):
        """
        Обрезает описание до 50 символов для удобного отображения.
        """
        return obj.description[:50] + "..." if len(obj.description) > 50 else obj.description

    description_short.short_description = "Краткое описание"

    fieldsets = (
        ("Основная информация", {"fields": ("name", "description")}),
        ("Финансовая информация", {"fields": ("price", "currency"), "classes": ("collapse",)}),
    )
