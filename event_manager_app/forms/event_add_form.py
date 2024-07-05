from typing import Any
from django import forms 
from django.core.validators import MinValueValidator, RegexValidator
import datetime

from event_management import settings

numeric = RegexValidator(r'^[0-9]')

class EventAdd(forms.Form):
   title =  forms.CharField(max_length=50)
   description =  forms.CharField(max_length=200)
   total_participants = forms.IntegerField(validators=[numeric])
   start_date = forms.CharField(widget=forms.TextInput(attrs={'class':'datepicker_start', 'autocomplete': 'off'}))

   end_date = forms.CharField(widget=forms.TextInput(attrs={'class':'datepicker_start', 'autocomplete': 'off'}))
   location =  forms.CharField(max_length=50)
   contact_person = forms.CharField(max_length=50)
   contact_number = forms.IntegerField(validators=[numeric])

   