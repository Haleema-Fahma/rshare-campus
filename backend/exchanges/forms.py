from django import forms
from .models import ExchangeRequest


class ExchangeRequestForm(forms.ModelForm):
    class Meta:
        model = ExchangeRequest
        fields = ["message", "requested_date"]

        widgets = {
            "message": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Tell the owner why you need this resource..."
                }
            ),
            "requested_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }