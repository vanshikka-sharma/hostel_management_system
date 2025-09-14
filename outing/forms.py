from django import forms
from .models import OutingApplication

class OutingApplicationForm(forms.ModelForm):
    class Meta:
        model = OutingApplication
        fields = ['outing_date', 'purpose', 'room_allotment']
        widgets = {
            'outing_date': forms.DateInput(attrs={'type': 'date'}),
            'purpose': forms.TextInput(attrs={'placeholder': 'Purpose of outing'}),
        }