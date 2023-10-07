from django.urls import path
from .views import OrderList , checkout ,add_to_cart

app_name = 'orders'

urlpatterns = [
    path('', OrderList.as_view()),
    path('checkout',checkout),
    path('add_to_cart', add_to_cart ,name ='add_to_cart'),
]
