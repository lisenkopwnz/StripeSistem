from django.urls import path

from item.views import ItemListView

app_name = 'items'

urlpatterns = [
    path('', ItemListView.as_view(), name='item_list'),

]