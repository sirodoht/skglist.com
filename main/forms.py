from django import forms

from .models import Place


class VoteForm(forms.ModelForm):
    class Meta:
        model = Place
