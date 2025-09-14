from django import forms
from .models import MessMenu

class MessMenuForm(forms.ModelForm):
    class Meta:
        model = MessMenu
        fields = ["day", "breakfast", "lunch", "dinner"]
