from django import forms
from .models import Account
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class RegistrationForm(forms.ModelForm): 
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    

    phone_number = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='GH')
    )
    class Meta:
        model = Account
        fields = ['first_name', 
                  'last_name', 
                  'phone_number', 
                  'email', 
                  'password',
                  'region']
    
    def clean(self):
        cleaned_data =super(RegistrationForm, self).clean()
        password =cleaned_data.get('password')
        confirm_password =cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('passwords do not match!')

    
  