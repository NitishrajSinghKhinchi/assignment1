from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser
from django import forms

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['name','email','address','dateofbirth','contact_number']
        labels = {'email': 'Email','name':'Username','address':'Address','dateofbirth':'Dob (year-m-d)'}
        widget={
            'dateofbirth':forms.DateField(input_formats=('%d-%m-%Y')),
        }

class EditUserProfileForm(UserChangeForm):
    password=None
    class Meta:
        model = CustomUser
        fields = ['name','email','address','dateofbirth','contact_number']
        labels = {'email': 'Email','name':'Username','address':'Address','dateofbirth':'Dob (year-m-d)','contact_number':'Phone number'}

        widget={
            'dateofbirth':forms.DateField(input_formats=('%d-%m-%Y')),
        }