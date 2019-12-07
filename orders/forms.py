from django.forms import ModelForm

from .models import OrderAddress



class OrderAddressForm(ModelForm):
    class Meta:
        model = OrderAddress
        fields = '__all__'
        

