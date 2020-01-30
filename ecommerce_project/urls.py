"""ecommerce_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path



urlpatterns = [

    # Admin urls 
    path('admin/', admin.site.urls),

    # account
    path('accounts/', include('allauth.urls')),

    # # users app
    # path('users/', include('users.urls')), # new
    # path('users/', include('django.contrib.auth.urls')),

    # products app urls
    path('', include('products.urls')),
    
    # carts app url
    path('cart/', include('carts.urls')),

    # orders app urls
    path('order/', include('orders.urls')),

    # directOrders app urls
    path('direct_order/', include('directOrders.urls')),

    # blog app
    path('blog/', include('blog.urls')),

    # ckeditor file upload
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

    
]

# Load static files in local development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
