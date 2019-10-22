from django.contrib import admin
from .models import DirectOrder

# Register your models here.
class DirectOrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'phone', 'status']

    class Meta:
        model = DirectOrder


admin.site.register(DirectOrder, DirectOrderAdmin)
