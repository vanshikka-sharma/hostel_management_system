from django import forms
from .models import VisitorRecord

class VisitorRecordForm(forms.ModelForm):
    class Meta:
        model = VisitorRecord
        fields = ['visitor_name', 'visitor_purpose', 'adhar_card_number', 'room_allotment']
        widgets = {
            'adhar_card_number': forms.TextInput(attrs={'maxlength': 16, 'pattern': '\\d{16}', 'title': 'Enter 16 digit Aadhaar number'}),
        }