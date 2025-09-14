# staff/forms.py
from django import forms
from .models import StaffMember, Shift, ShiftAssignment, SalaryRecord
from django.forms import DateInput, TimeInput

class StaffMemberForm(forms.ModelForm):
    class Meta:
        model = StaffMember
        fields = ['first_name','last_name','phone','email','address','staff_type','date_of_joining','photo']
        widgets = {
            'date_of_joining': DateInput(attrs={'type':'date'}),
        }

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['name','start_time','end_time','description']
        widgets = {
            'start_time': TimeInput(attrs={'type':'time'}),
            'end_time': TimeInput(attrs={'type':'time'}),
        }

class ShiftAssignmentForm(forms.ModelForm):
    class Meta:
        model = ShiftAssignment
        fields = ['shift','staff','date','notes']
        widgets = {'date': DateInput(attrs={'type':'date'})}

class SalaryRecordForm(forms.ModelForm):
    class Meta:
        model = SalaryRecord
        fields = ['staff','year','month','base_salary','allowances','deductions','holidays','off_days','notes']
