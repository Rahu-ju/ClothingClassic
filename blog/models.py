from django.conf import settings 
from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
def upload_blog_image(instance, filename):
    return 'blog/images/%s/%s' % (instance.id, filename)


class FeaturedPost(models.Model):
    '''The post shows in the blog page as slider.'''
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to=upload_blog_image)
    date = models.DateField(auto_now=False, auto_now_add=True)
    comment = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title



class Post(models.Model):

    '''For ususal blog posts..'''

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    # description = models.TextField(max_length=200)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to=upload_blog_image)
    date = models.DateField(auto_now=False, auto_now_add=True)
    comment = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='post_comments', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title



class Comment(models.Model):
    '''To handle posts comment by annonymous or signed in user.'''

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    comment = models.TextField()
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name
    

    

