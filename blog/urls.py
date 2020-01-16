from django.urls import path

from .views import posts, post_detail


urlpatterns = [
    path('', posts, name='posts'),
    path('post_detail/', post_detail, name='post_detail'),
]