from django.contrib import admin

from .models import FeaturedPost, Post, Comment

# Register your models here.
admin.site.register(FeaturedPost)
admin.site.register(Post)
admin.site.register(Comment)
