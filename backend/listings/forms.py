from django import forms
from .models import Listing


class ListingForm(forms.ModelForm):

    class Meta:
        model = Listing

        fields = [
            "listing_type",
            "title",
            "description",
            "category",
            "image",
            "condition",
            "credit_cost",
            "duration_days",
            "location",
        ]

        widgets = {

            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Describe your resource or skill..."
                }
            ),

            "credit_cost": forms.NumberInput(
                attrs={
                    "min": 1
                }
            ),

            "duration_days": forms.NumberInput(
                attrs={
                    "min": 1
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "placeholder": "e.g. RCSS Library"
                }
            ),
        }