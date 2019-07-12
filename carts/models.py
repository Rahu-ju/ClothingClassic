from django.db import models

from products.models import Product

# Create your models here.
class CartItem(models.Model):
    cart = models.ForeignKey('cart', on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    line_total = models.DecimalField( max_digits=100, decimal_places=2, default=10.00)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.product.title
    


class Cart(models.Model):
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "Cart id: %s" %(self.id)
    