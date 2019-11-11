from django.db import models
from django.urls import reverse

# Create your models here.
VAR_CATEGORIES = (
    ("abc", "abc"),
    ("liquid", "liquid"),
    ("cloth", "cloth"),
)

class Product(models.Model):
    category = models.CharField(max_length=50, choices=VAR_CATEGORIES, default='abc')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=50, decimal_places=2, default=29.99)
    sale_price = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    active = models.BooleanField(default=True)
    show_in_homepage = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'slug')

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def get_image_url(self):
        return self.productimage_set.all()[0].image.url



class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images')
    feature = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.product.title



# objects manager for variation model
class VariationManager(models.Manager):
    
    def all(self):
        return super(VariationManager, self).filter(active=True)
    
    def sizes(self):
        return self.all().get('size')

    def colors(self):
        return self.all().get('color')

    def types(self):
        return self.all().get('types')


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ForeignKey(ProductImage, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=120, null=True, blank=True)
    size = models.CharField(max_length=120, null=True, blank=True)
    color = models.CharField(max_length=120, null=True, blank=True)
    types = models.CharField(max_length=120, null=True, blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    active = models.BooleanField(default=True)

    objects = VariationManager()

    def __str__(self):
        return self.product.title
    
    