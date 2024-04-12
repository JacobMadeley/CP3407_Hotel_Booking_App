from django import forms
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Hotel
from .models import RoomType
from .models import Booking
from .models import Guest
from .models import Room
from django.utils import timezone
# from .models import Record


class BookingForm(forms.Form):
    start_date = forms.DateField(label='start date', initial=datetime.date.today)
    end_date = forms.DateField(label='end date', initial=datetime.date.today)
    adults_number = forms.IntegerField(label='Adults', max_value=10)
    children_number = forms.IntegerField(label='Children', max_value=10)
    guest_title = forms.CharField(label= 'title',max_length=10)
    guest_first_name = forms.CharField(label='first name',max_length=50)
    guest_last_name = forms.CharField(label='last name',max_length=50)
    guest_date_of_birth = forms.DateField(label='date of birth',initial=timezone.now)
    guest_phone_number = forms.CharField(label='phone number',max_length=20)
    guest_email = forms.EmailField(label='email')
    guest_address = forms.CharField(label='address',max_length=50)
    guest_city = forms.CharField(label='city',max_length=50)
    guest_state = forms.CharField(label='state',max_length=50)
    guest_country = forms.CharField(label='country',max_length=50)
    guest_postcode = forms.CharField(label='postcode',max_length=10)
    room = forms.ModelChoiceField(label= 'room', queryset=Room.objects, required=True)


class AddRoomType(forms.Form):
    room_type_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Room Type", "class":"form-control"}), label="",error_messages={'required': ''}, max_length=100)
    room_type_description = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Room Description", "class":"form-control"}), label="",error_messages={'required': ''}, max_length=150)
    room_type_price = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Room Price", "class":"form-control"}), label="",error_messages={'required': ''}, max_value=1000)
    room_image_url = forms.ImageField(label='Room Image')
    
    
class AddRoom(forms.Form):
    room_number = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Room Number", "class":"form-control"}), label="",error_messages={'required': ''})
    room_status = forms.ChoiceField(required=True, label='Room Status', choices=[(1,'Occupied'), (2,'Free'),(3,'Needs Cleaning'), (4,'Needs Maintenance')], widget=forms.Select(attrs={"class": "form-control"}))
    hotel = forms.ModelChoiceField(label= 'Hotel', queryset=Hotel.objects, required=False, widget=forms.Select(attrs={"class": "form-control"}))
    room_type = forms.ModelChoiceField(label='Room Type', queryset=RoomType.objects, required=False, widget=forms.Select(attrs={"class": "form-control"}))

class PaymentForm(forms.Form):
    payment_date = forms.DateField(label='date',initial=timezone.now)
    payment_card_number = forms.CharField(label= 'Card Number')
    payment_card_expiry_date = forms.DateField(label='Card Expiry')
    payment_for_booking = forms.DecimalField(label='booking cost',max_digits=20, decimal_places=2, disabled=True, initial=200)
    payment_for_service = forms.DecimalField(label='service cost',max_digits=20, decimal_places=2, disabled=True, initial=50)
    payment_for_bar = forms.DecimalField(label='bar tab',max_digits=20, decimal_places=2, disabled=True, initial=20)
    payment_for_late_check_out = forms.DecimalField(label='late checkout',max_digits=20, decimal_places=2, disabled=True, initial=0)
    payment_for_miscellaneous = forms.DecimalField(label='misc costs',max_digits=20, decimal_places=2, disabled=True, initial=0)
    payment_for_miscellaneous_description = forms.CharField(label='misc cost description', disabled=True, initial='N/A')
    booking = forms.ModelChoiceField(label= 'booking', queryset=Booking.objects, disabled=True, widget=forms.HiddenInput())
    guest = forms.ModelChoiceField(label= 'guest', queryset = Guest.objects, disabled=True,widget=forms.HiddenInput())
    


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




class AddRecordForm(forms.ModelForm):
	# first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
	# last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
	# email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
	# phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
	# address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
	# city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
	# state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="")
	# zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), label="")



    hotel_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Hotel Name", "class":"form-control"}), label="",error_messages={'required': ''})
    hotel_address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Hotel Address", "class":"form-control"}), label="",error_messages={'required': ''})
    hotel_city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Hotel City", "class":"form-control"}), label="",error_messages={'required': ''})
    hotel_country = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Hotel Country", "class":"form-control"}), label="",error_messages={'required': ''})
    hotel_postcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Hotel Postcode", "class":"form-control"}), label="",error_messages={'required': ''})
    hotel_phone_number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Hotel Phone Number", "class":"form-control"}), label="",error_messages={'required': ''})
    hotel_star_rating = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Hotel Star Rating", "class":"form-control"}), label="",error_messages={'required': ''})

    class Meta:
        model = Hotel
        exclude = ("hotel",)
    

class UpdateRoomStatus(forms.Form):
    room_number = forms.IntegerField(required=True,label='room number')
    room_status = forms.ChoiceField(label='room status', choices=[(1,'occupied'), (2,'free'),(3,'needs cleaning'), (4,'needs maintenance')])