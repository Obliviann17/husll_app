from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField


from .models import *



# Create form

class NewUserForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True, help_text='Required. Enter a valid email address.', widget=forms.TextInput(attrs={'placeholder': 'exsample1@gmail.com'}))
    first_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your first name.', widget=forms.TextInput(attrs={'placeholder': 'Введіть свое ім\'я'}))
    last_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your last name.', widget=forms.TextInput(attrs={'placeholder': 'Введіть своє прізвище'}))
    phone = PhoneNumberField()
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'phone', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs['placeholder'] = '+380501267830'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone = self.cleaned_data.get('phone')
        if commit:
            user.save()
        return user

