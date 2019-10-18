from django.contrib import admin
from .models import Slider

# Register your models here.

class SliderAdmin(admin.ModelAdmin):
    list_display = ["__str__", "slider_order", "active"]
    list_editable = ["slider_order"]

    class Meta:
        model = Slider
    
admin.site.register(Slider, SliderAdmin)