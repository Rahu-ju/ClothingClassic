from django.conf import settings
from django.db import models

# Create your models here.
def slider_upload(instance, filename):
    return "img/slider/marketing/%s" %(filename)

class Slider(models.Model):
    image = models.ImageField(upload_to=slider_upload, height_field=None, width_field=None, max_length=None)
    slider_order = models.IntegerField(default=0)
    header_text = models.CharField(max_length=150, null=True, blank=True)
    text = models.CharField(max_length=150, null=True, blank=True)
    active = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    updated = models.DateField(auto_now=True, auto_now_add=False)
    start_date = models.DateField(auto_now=False, auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    def get_image_url(self):
        return "%s/%s" %(settings.MEDIA_URL, self.image)
    

