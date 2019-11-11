from django.contrib import admin

from .models import Product, ProductImage, Variation

# Register your models here.
# class ProductImageInline(admin.StackedInline):
#     model = ProductImage



# class VariationsInline(admin.StackedInline):
#     model = Variation



class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    search_fields = ['title', 'description'] # Give search widget 
    list_display = ['__str__','title', 'price', 'timestamp', 'active']
    list_editable = ['active']
    list_filter = ['price', 'active'] #Show the filter widget with filter option
    # inlines = [ProductImageInline, VariationsInline,]
    class Meta:
        model = Product
    
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Variation)
