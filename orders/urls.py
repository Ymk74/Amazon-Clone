from django.urls import path
from .views import OrderList , checkout ,add_to_cart , remove_from_cart
from .api import CartDetailCreateAPI , OrderListAPI , OrderDetailAPI , CreateOrderAPI , ApplyCouponAPI 



app_name = 'orders'

urlpatterns = [
    path('', OrderList.as_view()),
    path('checkout',checkout),
    path('add_to_cart', add_to_cart ,name ='add_to_cart'),
    path('<int:id>/remove-from-cart',remove_from_cart),


    # api  
    path('api/list/<str:username>',OrderListAPI.as_view()),
    path('api/list/<str:username>/create-order',CreateOrderAPI.as_view()),
    path('api/<str:username>/cart', CartDetailCreateAPI.as_view()),
    path('api/<str:username>/cart/apply-coupon', ApplyCouponAPI.as_view()),
    path('api/list/<str:username>/<int:pk>',OrderDetailAPI.as_view()),
]
