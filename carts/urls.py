from django.urls import path

from . import views



urlpatterns = [
    path('', views.cart, name='cart'),
    path('update/', views.update_cart_item, name='update_cart_item'),
    path('add_to_cart/<slug>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    
]