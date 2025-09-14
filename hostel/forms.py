from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Profile

class RegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)

    name = forms.CharField(max_length=100)
    father_name = forms.CharField(max_length=100)
    mother_name = forms.CharField(max_length=100)
    course = forms.CharField(max_length=100)
    branch = forms.CharField(max_length=100)
    city_name = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    parents_phone_no = forms.CharField(max_length=15)
    phone_no = forms.CharField(max_length=15)
    college_roll_no = forms.CharField(max_length=50)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'role',
                  'name', 'father_name', 'mother_name', 'course', 'branch', 'city_name',
                  'state', 'parents_phone_no', 'phone_no', 'college_roll_no')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = self.cleaned_data['role']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                name=self.cleaned_data['name'],
                father_name=self.cleaned_data['father_name'],
                mother_name=self.cleaned_data['mother_name'],
                course=self.cleaned_data['course'],
                branch=self.cleaned_data['branch'],
                city_name=self.cleaned_data['city_name'],
                state=self.cleaned_data['state'],
                parents_phone_no=self.cleaned_data['parents_phone_no'],
                phone_no=self.cleaned_data['phone_no'],
                college_roll_no=self.cleaned_data['college_roll_no'],
            )
        return user


