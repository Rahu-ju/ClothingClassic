from django.forms import ModelForm, TextInput, EmailInput, NumberInput, Textarea
from .models import DirectOrder


class DirectOrderForm(ModelForm):
    class Meta:
        model = DirectOrder
        fields = '__all__'
        widgets = {
            "name": TextInput(attrs={"placeholder": "Your nick name",
                                    "class": "form-control",}),
            "email": EmailInput(attrs={"placeholder": "Your mail to contact with you.",
                                    "class": "form-control",}),
            "phone": NumberInput(attrs={"placeholder": "Your phone number",
                                    "class": "form-control",}),
            "amount": NumberInput(attrs={"placeholder": "Your amount in Kg",
                                    "class": "form-control amount",}),                        
            "address": Textarea(attrs={"placeholder": "You will get your products to this address.",
                                    "class": "form-control",
                                    "rows":"3",}),
            "say": Textarea(attrs={"placeholder": "What's on your mind!.",
                                    "class": "form-control",
                                    "rows":"3",}),

        }

