from django.forms import ModelForm, TextInput, EmailInput, NumberInput, Textarea
from .models import OrderAddress


class OrderAddressForm(ModelForm):
    class Meta:
        model = OrderAddress
        fields = '__all__'
        widgets = {
            "name": TextInput(attrs={"placeholder": "Your nick name",
                                    "class": "form-control",}),
            "phone": NumberInput(attrs={"placeholder": "Your phone number",
                                    "class": "form-control",}),                           
            "address": Textarea(attrs={"placeholder": "You will get your products to this address.",
                                    "class": "form-control",
                                    "rows":"3",}),
            "comment": Textarea(attrs={"placeholder": "What's on your mind!.",
                                    "class": "form-control",
                                    "rows":"3",}),
            "email": EmailInput(attrs={"placeholder": "Your mail to contact with you.",
                                    "class": "form-control",}),                      

        }

