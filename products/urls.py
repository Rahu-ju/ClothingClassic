from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('all_products/', views.products, name='products'),
    path('products/<slug>/', views.detail, name='detail'),
]