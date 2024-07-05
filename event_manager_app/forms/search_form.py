from django import forms 
from django.core.validators import MinValueValidator, RegexValidator
import datetime

from event_management import settings
from event_manager_app.utils import getdata, setdata 

numeric = RegexValidator(r'^[0-9]')
data = getdata()
end_dates = [(item['end_date'], item['end_date']) for item in data]
start_date = [(item['start_date'], item['start_date']) for item in data]

class SearchForm(forms.Form):
   title =  forms.CharField(max_length=50, required=False)
   start_dates = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,
                                 widget=forms.TextInput(attrs={ 'class': 'datepicker_start', 'autocomplete': 'off'}),required=False)
   end_date =  forms.ChoiceField(choices=end_dates, required=False)
   
   
   