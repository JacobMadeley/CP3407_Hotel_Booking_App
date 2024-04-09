from django import forms
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Hotel
from .models import RoomType
from .models import Booking
from .models import Guest
from django.utils import timezone
# from .models import Record


class BookingForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    start_date = forms.DateField(label='start date', initial=datetime.date.today)
    end_date = forms.DateField(label='end date', initial=datetime.date.today)
    adults_number = forms.IntegerField(label='Adults', max_value=10)
    children_number = forms.IntegerField(label='Children', max_value=10)

class AddRoomType(forms.Form):
    room_type_name = forms.CharField(label='room type', max_length=100)
    room_type_description = forms.CharField(label='description', max_length=150)
    room_type_price = forms.IntegerField(label='price', max_value=1000)
    room_image_url = forms.URLField(label='Image URL')
    
class AddRoom(forms.Form):
    room_number = forms.IntegerField(label='room number')
    room_status = forms.CharField(label='room status', max_length=100)
    #hotel = forms(Hotel, on_delete=models.CASCADE)
    #room_type = models.ForeignKey('RoomType', on_delete=models.CASCADE)
    hotel = forms.ModelChoiceField(label= 'hotel', queryset=Hotel.objects, required=False)
    room_type = forms.ModelChoiceField(label='room type', queryset=RoomType.objects, required=False)

class PaymentForm(forms.Form):
    payment_date = forms.DateField(label='date',initial=timezone.now)
    payment_card_number = forms.CharField(label= 'Card Number')
    payment_card_expiry_date = forms.DateField(label='Card Expiry')
    #payment_for_booking = forms.DecimalField(max_digits=20, decimal_places=2)
    #payment_for_service = forms.DecimalField(max_digits=20, decimal_places=2)
    #payment_for_bar = forms.DecimalField(max_digits=20, decimal_places=2)
    #payment_for_late_check_out = forms.DecimalField(max_digits=20, decimal_places=2)
    #payment_for_miscellaneous = forms.DecimalField(max_digits=20, decimal_places=2)
    #payment_for_miscellaneous_description = forms.CharField()
    #booking = forms.ModelChoiceField(label= 'booking', queryset=Booking.objects)
    #guest = forms.MultipleChoiceField(label= 'guest', queryset = Guest.objects)


class SignUpForm(UserCreationForm):
	# email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	# first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	# last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	# class Meta:
	# 	model = User
	# 	fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	




# Create Add Record Form
# class AddRecordForm(forms.ModelForm):
# 	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
# 	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
# 	email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
# 	phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
# 	address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
# 	city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
# 	state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="")
# 	zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), label="")

# 	class Meta:
# 		model = Record
# 		exclude = ("user",)