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


class BookingForm(forms.Form):
    start_date = forms.DateField(label='Start Date', initial=datetime.date.today,widget=forms.DateInput(attrs={"class": "form-control"}))
    end_date = forms.DateField(label='End Date', initial=datetime.date.today,widget=forms.DateInput(attrs={"class": "form-control"}))
    adults_number = forms.IntegerField(label='Adults', max_value=10,widget=forms.NumberInput(attrs={"class": "form-control"}))
    children_number = forms.IntegerField(label='Children', max_value=10,widget=forms.NumberInput(attrs={"class": "form-control"}))
    guest_title = forms.CharField(label= 'Title',max_length=10,widget=forms.TextInput(attrs={"class": "form-control"}))
    guest_first_name = forms.CharField(label='First Name',max_length=50,widget=forms.TextInput(attrs={"class": "form-control"}))
    guest_last_name = forms.CharField(label='Last Name',max_length=50,widget=forms.TextInput(attrs={"class": "form-control"}))
    guest_date_of_birth = forms.DateField(label='Date of Birth',initial=timezone.now,widget=forms.DateInput(attrs={"class": "form-control"}))
    guest_phone_number = forms.CharField(label='Phone Number',max_length=20,widget=forms.TextInput(attrs={"class": "form-control"}))
    guest_email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={"class": "form-control"}))
    guest_address = forms.CharField(label='Address',max_length=50,widget=forms.TextInput(attrs={"class": "form-control"}))
    guest_city = forms.CharField(label='City',max_length=50,widget=forms.TextInput(attrs={"class": "form-control"}))
    guest_state = forms.CharField(label='State',max_length=50,widget=forms.TextInput(attrs={"class": "form-control"}))
    guest_country = forms.CharField(label='Country',max_length=50,widget=forms.TextInput(attrs={"class": "form-control"}))
    guest_postcode = forms.CharField(label='Postcode',max_length=10,widget=forms.TextInput(attrs={"class": "form-control"}))
    room = forms.ModelChoiceField(label= 'Room', queryset=Room.objects, required=True,widget=forms.Select(attrs={"class": "form-control"}))


class AddRoomType(forms.Form):
    room_type_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Room Type", "class":"form-control"}), label="",error_messages={'required': ''}, max_length=100)
    room_type_description = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Room Description", "class":"form-control"}), label="",error_messages={'required': ''}, max_length=150)
    room_type_price = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Room Price", "class":"form-control"}), label="",error_messages={'required': ''}, max_value=1000)
    room_image_url = forms.ImageField(label='Room Image')
    
    
class AddRoom(forms.Form):
    room_number = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Room Number", "class":"form-control"}),label="",error_messages={'required': ''})
    room_status = forms.ChoiceField(required=True, label='Room Status', choices=[(1,'Occupied'), (2,'Free'),(3,'Needs Cleaning'), (4,'Needs Maintenance')],widget=forms.Select(attrs={"class": "form-control"}))
    hotel = forms.ModelChoiceField(label= 'Hotel', queryset=Hotel.objects, required=False,widget=forms.Select(attrs={"class": "form-control"}))
    room_type = forms.ModelChoiceField(label='Room Type', queryset=RoomType.objects, required=False,widget=forms.Select(attrs={"class": "form-control"}))


class PaymentForm(forms.Form):
    payment_date = forms.DateField(label='Date', initial=timezone.now,widget=forms.DateInput(attrs={"class": "form-control"}))
    payment_card_number = forms.CharField(label='Card Numeber',max_length=50,widget=forms.TextInput(attrs={"class": "form-control"}))
    payment_card_expiry_date = forms.DateField(label='Card Expire Date', widget=forms.DateInput(attrs={"class": "form-control"}))


    payment_for_booking = forms.DecimalField(label='booking cost',max_digits=20, decimal_places=2, disabled=True, initial=200, widget=forms.DateInput(attrs={"class": "form-control"}))
    payment_for_service = forms.DecimalField(label='service cost',max_digits=20, decimal_places=2, disabled=True, initial=50, widget=forms.DateInput(attrs={"class": "form-control"}))
    payment_for_bar = forms.DecimalField(label='bar tab',max_digits=20, decimal_places=2, disabled=True, initial=20, widget=forms.DateInput(attrs={"class": "form-control"}))
    payment_for_late_check_out = forms.DecimalField(label='late checkout',max_digits=20, decimal_places=2, disabled=True, initial=0, widget=forms.DateInput(attrs={"class": "form-control"}))
    payment_for_miscellaneous = forms.DecimalField(label='misc costs',max_digits=20, decimal_places=2, disabled=True, initial=0, widget=forms.DateInput(attrs={"class": "form-control"}))
    payment_for_miscellaneous_description = forms.CharField(label='Misc Cost Description', disabled=True, initial='N/A', widget=forms.DateInput(attrs={"class": "form-control"}))


    
    booking = forms.ModelChoiceField(label='Booking', queryset=Booking.objects, disabled=True, widget=forms.HiddenInput(attrs={"class": "form-control"}))
    guest = forms.ModelChoiceField(label= 'guest', queryset = Guest.objects, disabled=True,widget=forms.HiddenInput())
    

class SignUpForm(UserCreationForm):
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
    room_id = forms.IntegerField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Room ID", "class":"form-control"}), label="",error_messages={'required': ''})
    room_status = forms.ChoiceField(required=True, label='Room Status', choices=[(1,'Occupied'), (2,'Free'),(3,'Needs Cleaning'), (4,'Needs Maintenance')], widget=forms.Select(attrs={"class": "form-control"}))
