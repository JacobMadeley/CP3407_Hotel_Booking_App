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
    payment_for_booking = forms.DecimalField(label='booking cost',max_digits=20, decimal_places=2, disabled=True, initial=200)
    payment_for_service = forms.DecimalField(label='service cost',max_digits=20, decimal_places=2, disabled=True, initial=50)
    payment_for_bar = forms.DecimalField(label='bar tab',max_digits=20, decimal_places=2, disabled=True, initial=20)
    payment_for_late_check_out = forms.DecimalField(label='late checkout',max_digits=20, decimal_places=2, disabled=True, initial=0)
    payment_for_miscellaneous = forms.DecimalField(label='misc costs',max_digits=20, decimal_places=2, disabled=True, initial=0)
    payment_for_miscellaneous_description = forms.CharField(label='misc cost description', disabled=True, initial='N/A')
    booking = forms.ModelChoiceField(label= 'booking', queryset=Booking.objects, disabled=True)
    guest = forms.ModelChoiceField(label= 'guest', queryset = Guest.objects, disabled=True)


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



    hotel_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Hotel Name", "class":"form-control"}), label="")
    hotel_address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Hotel Address", "class":"form-control"}), label="")
    hotel_city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Hotel City", "class":"form-control"}), label="")
    hotel_country = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Hotel Country", "class":"form-control"}), label="")
    hotel_postcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Hotel Postcode", "class":"form-control"}), label="")
    hotel_phone_number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Hotel Phone Number", "class":"form-control"}), label="")
    hotel_star_rating = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Hotel Star Rating", "class":"form-control"}), label="")

    class Meta:
        model = Hotel
        exclude = ("hotel",)
    

