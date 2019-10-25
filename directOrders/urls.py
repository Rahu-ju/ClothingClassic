from django.urls import path

from .views import direct_checkout, order_confirm



urlpatterns = [
    path('', direct_checkout, name='direct_order'),
    path('order_confirm/', order_confirm, name='order_confirm'),
]