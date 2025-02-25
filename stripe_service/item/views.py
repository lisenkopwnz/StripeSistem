from django.views.generic import ListView

from item.models import Item


class ItemListView(ListView):
    model = Item
    template_name = "item/items_list.html"
    context_object_name = "items"
    paginate_by = 20
