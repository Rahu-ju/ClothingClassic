from django.db import models
from django.contrib.auth import get_user_model
from carts.models import Cart

# Create your models here.
User = get_user_model()

STATUS_CHOICES = (
    ('Started', 'Started'),
    ('Abandoned', 'Abandoned'),
    ('Finished', 'Finished'),
)
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    order_id = models.CharField(max_length=50, default='abc', unique=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Started')
    #address
    sub_total = models.DecimalField(max_digits=100, decimal_places=2, default=10.00)
    tax_total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    final_total = models.DecimalField(max_digits=100, decimal_places=2, default=10.00)
    
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.order_id
    

