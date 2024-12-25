from django import forms
from .models import Hotel


class AddHotel(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = [
            'name',
            'address'
        ]
