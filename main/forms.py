from django import forms

from . import models


class PlaceForm(forms.ModelForm):
    class Meta:
        model = models.Place
        fields = ["name", "address", "link", "is_eat", "is_drink"]
