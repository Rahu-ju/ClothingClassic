from django.contrib import admin

from .models import Order, OrderAddress

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderAddress)
