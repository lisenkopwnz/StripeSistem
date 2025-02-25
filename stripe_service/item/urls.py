from django.urls import path

from item.views import ItemListView

urlpatterns = [
    path('', ItemListView.as_view(), name='item_list'),

]