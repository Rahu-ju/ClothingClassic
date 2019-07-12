from django.urls import path

from . import views



urlpatterns = [
    path('', views.view, name='cart'),
    path('<slug>/', views.update_cart, name='cart_update'),
]