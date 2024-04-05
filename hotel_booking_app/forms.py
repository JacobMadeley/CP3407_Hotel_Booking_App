from django import forms
import datetime

class BookingForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    start_date = forms.DateField(label='start date', initial=datetime.date.today)
    end_date = forms.DateField(label='end date', initial=datetime.date.today)
    adults_number = forms.IntegerField(label='Adults', max_value=10)
    children_number = forms.IntegerField(label='Children', max_value=10)