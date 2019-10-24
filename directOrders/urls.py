from django.urls import path

from .views import direct_checkout



urlpatterns = [
    path('', direct_checkout, name='direct_order'),
]