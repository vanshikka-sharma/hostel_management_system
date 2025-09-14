from django import forms
from .models import StaffMember

class StaffForm(forms.ModelForm):
    class Meta:
        model = StaffMember
        fields = ['name', 'address', 'role', 'shift', 'contact']


