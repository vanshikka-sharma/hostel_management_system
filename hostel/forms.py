from django import forms
from django.core.exceptions import ValidationError

from .models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = [
            'username', 'name', 'adhaar_card_number', 'email', 'phone_number', 'parents_name',
            'parents_phone_number', 'city', 'state', 'alternate_phone_number', 'college_roll_no',
            'branch', 'course', 'role', 'password'
        ]

    # All custom validation restrictions removed

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


