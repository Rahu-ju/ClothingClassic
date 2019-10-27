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
            "address": Textarea(attrs={"placeholder": "we will send your order to this address.",
                                    "class": "form-control",}),
            "say": Textarea(attrs={"placeholder": "we will happy to take your suggestions.",
                                    "class": "form-control",}),

        }

