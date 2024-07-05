from django import forms 
from django.core.validators import MinValueValidator, RegexValidator
import datetime

numeric = RegexValidator(r'^[0-9]')

class UserLoginForm(forms.Form):
   username =  forms.CharField(max_length=50)
   password =  forms.CharField(max_length=200, widget=forms.PasswordInput())
   