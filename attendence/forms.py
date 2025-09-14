from django import forms
from .models import Attendance

class AttendanceDateForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['present']
