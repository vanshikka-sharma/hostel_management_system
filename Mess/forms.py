from django import forms
from .models import MessMenu

class MessMenuForm(forms.ModelForm):
    breakfast = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    lunch = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    dinner = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = MessMenu
        fields = ["day", "breakfast", "lunch", "dinner"]
