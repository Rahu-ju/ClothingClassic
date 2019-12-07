from django.urls import path
from .views import checkout, orders, order_detail, order_confirm


urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('all/', orders, name='orders'),
    path('order_detail/', order_detail, name='order_detail'),
    path('OrderConfirmed/', order_confirm, name='order_confirmed'),
]