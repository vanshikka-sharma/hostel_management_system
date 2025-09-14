from django import forms
from .models import HostelAllotment, User

class HostelAllotmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(role='student')
    security_fees = forms.DecimalField(max_digits=8, decimal_places=2)
    allotment_fees = forms.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        model = HostelAllotment
        fields = ['security_fees', 'allotment_fees', 'user']

    def clean(self):
        cleaned_data = super().clean()
        security_fees = cleaned_data.get('security_fees')
        allotment_fees = cleaned_data.get('allotment_fees')
        if security_fees is not None and allotment_fees is not None:
            cleaned_data['total_payable'] = security_fees + allotment_fees
        return cleaned_data
