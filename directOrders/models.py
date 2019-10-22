from django.db import models
from django.conf import settings

# Create your models here.
STATUS_CHOICES = (
    ('Started', 'Started'),
    ('Abandoned', 'Abandoned'),
    ('Finished', 'Finished'),
)

class DirectOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone = models.IntegerField()
    address = models.TextField(max_length=150)
    say = models.TextField(max_length=150, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Started')
    order_id = models.CharField(max_length=50, default='abc', unique=True)

    def __str__(self):
        return self.name
    

