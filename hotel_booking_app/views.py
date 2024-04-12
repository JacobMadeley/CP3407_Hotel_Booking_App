from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .forms import BookingForm
from .models import Guest
from .models import Hotel
from .models import Booking
from .models import Inventory
from .models import Room
from .models import RoomType
from .models import Payment
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .forms import AddRoomType
from .forms import AddRoom
from .forms import PaymentForm
from .forms import AddRecordForm
# Create your views here.


def home(request):
	# records = Record.objects.all()
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
            
			return redirect('dashboard')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
            
			return redirect('dashboard')
	else:

		return render(request, 'dashboard.html')




def  login_user(request):
    
    pass

def logout_user(request):
    

	logout(request)
	messages.success(request, "You Have Been Logged Out...")
    
	return redirect('dashboard')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def add_record(request):
	form = AddRecordForm(request.POST, request.FILES)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('dashboard')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('dashboard')

def inventory(request):
    #rooms = Inventory.objects.all().values()
    #template = loader.get_template('inventory.html')
    #context = {
    #'rooms': rooms,
    #}
    if request.method =='POST':
        form = AddRoomType(request.POST, request.FILES)
        if form.is_valid():
            room_type_name = form.cleaned_data['room_type_name']
            room_type_description = form.cleaned_data['room_type_description']
            room_type_price = form.cleaned_data['room_type_price']
            image_url = form.cleaned_data['room_image_url']
            print(room_type_name)
            print(room_type_description)
            print(room_type_price)
            room_type = RoomType(room_type_name = room_type_name, room_type_description = room_type_description, room_type_images = image_url, room_type_price = room_type_price)
            room_type.save()
    else:
        form = AddRoomType()

    inventorys = Inventory.objects.all()
    rooms = Room.objects.all()
    roomtypes = RoomType.objects.all()
    return render(request, 'inventory.html', 
    {'inventorys': inventorys, 'rooms': rooms, 'roomtypes': roomtypes, 'form': form, 'form2':AddRoom()})

def dashboard(request):
    # return render(request, "dashboard.html")
    hotels = Hotel.objects.all()
    roomtypes = RoomType.objects.all()

    return render(request, 'dashboard.html', {'hotels': hotels, 'roomtypes': roomtypes})

def booking(request):
    hotels = Hotel.objects.all()
    return render(request, "booking.html", {'hotels': hotels})


def user(request):
    hotels = Hotel.objects.all()
    return render(request, "user.html", {'hotels': hotels})
    #
    # users = Guest.objects.all()
    # return render(request, 'user.html', {'users': users})

def contact(request):
    hotels = Hotel.objects.all()
    return render(request, "contact.html", {'hotels': hotels})




def add_room(request):
    
    if request.method == 'POST':
        form = AddRoom(request.POST)
        if form.is_valid():
            room_num = form.cleaned_data['room_number']
            room_status = form.cleaned_data['room_status']
            hotel = form.cleaned_data['hotel']
            room_type = form.cleaned_data['room_type']
            
            room = Room(room_number = str(room_num), room_status = room_status, hotel = hotel, room_type = room_type)
            room.save()
            
    form = AddRoomType()
    form2 = AddRoom()
    hotels = Hotel.objects.all()
    inventorys = Inventory.objects.all()
    rooms = Room.objects.all()
    roomtypes = RoomType.objects.all()
    return render(request, 'inventory.html', 
    {'inventorys': inventorys, 'rooms': rooms,'hotels': hotels, 'roomtypes': roomtypes, 'form': form,'form2':form2})

def users(request):
    return render(request, "users.html")

def make_booking(request):
    if request.method =='POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            start = form.cleaned_data['start_date']
            end = form.cleaned_data['end_date']
            adults = form.cleaned_data['adults_number']
            children = form.cleaned_data['children_number']
            guest_title=form.cleaned_data['guest_title']
            guest_first_name=form.cleaned_data['guest_first_name']
            guest_last_name=form.cleaned_data['guest_last_name']
            guest_date_of_birth=form.cleaned_data['guest_date_of_birth']
            guest_phone_number=form.cleaned_data['guest_phone_number']
            guest_email=form.cleaned_data['guest_email']
            guest_address=form.cleaned_data['guest_address']
            guest_city=form.cleaned_data['guest_city']
            guest_state=form.cleaned_data['guest_state']
            guest_country=form.cleaned_data['guest_country']
            guest_postcode=form.cleaned_data['guest_postcode']
            room=form.cleaned_data['room']
            print(start)
            print(end)
            print(adults)
            print(children)
            booking_request = Booking(booking_check_in = start, booking_check_out = end, booking_number_of_adults = adults, booking_number_of_children = children)
            guest = Guest(guest_title=guest_title, guest_first_name=guest_first_name, guest_last_name=guest_last_name, guest_date_of_birth=guest_date_of_birth, guest_phone_number=guest_phone_number, guest_email=guest_email, guest_address=guest_address, guest_city=guest_city, guest_state=guest_state, guest_country=guest_country, guest_postcode=guest_postcode, booking=booking_request)
            inventory_entry = Inventory(hotel = room.hotel,room = room,booking = booking_request, guest=guest)
            #try:
            booking_request.save()
            guest.save()
            inventory_entry.save()
            request.session['guest_id'] = [guest.guest_id,booking_request.booking_id]
            #except:
            #    print('booking failed')

            Booking.objects.all().values()
            return HttpResponseRedirect('/payment/')
    else:
        form = BookingForm()
    hotels = Hotel.objects.all()
    return render(request, 'make_booking.html', {'form': form, 'hotels': hotels})

def payments(request):
    if request.method=='POST':
        guest_id = request.session.get('guest_id')
        print(guest_id)

        booking = Booking.objects.all()[guest_id[1]-1]
        guest= Guest.objects.all()[guest_id[0]-1]
        form = PaymentForm(initial={'booking':booking,'guest':guest})

        form = PaymentForm(request.POST,initial={'booking':booking,'guest':guest})
        if form.is_valid():
            payment_date = form.cleaned_data['payment_date']
            
            payment_card_number = form.cleaned_data['payment_card_number']
            payment_card_expiry_date = form.cleaned_data['payment_card_expiry_date']
            payment_for_booking = form.cleaned_data['payment_for_booking']
            payment_for_service = form.cleaned_data['payment_for_service']
            payment_for_bar = form.cleaned_data['payment_for_bar']
            payment_for_late_check_out = form.cleaned_data['payment_for_late_check_out']
            payment_for_miscellaneous = form.cleaned_data['payment_for_miscellaneous']
            payment_for_miscellaneous_description = form.cleaned_data['payment_for_miscellaneous_description']
            booking2 = form.cleaned_data['booking']
            guest2 = form.cleaned_data['guest']
            payment = Payment(payment_date=payment_date, payment_card_number=payment_card_number, payment_card_expiry_date=payment_card_expiry_date, payment_for_booking=payment_for_booking, payment_for_service=payment_for_service, payment_for_bar=payment_for_bar, payment_for_late_check_out=payment_for_late_check_out, payment_for_miscellaneous=payment_for_miscellaneous, payment_for_miscellaneous_description=payment_for_miscellaneous_description, booking=booking2, guest = guest2)
            payment.save()
            print(3)
            
    else:
        guest_id = request.session.get('guest_id')
        print(guest_id)
        try:
            booking = Booking.objects.all()[guest_id[1]-1]
            guest= Guest.objects.all()[guest_id[0]-1]
            form = PaymentForm(initial={'booking':booking,'guest':guest})
        except:
            return HttpResponseRedirect('/make_booking/')
    try:        
        return render(request, "payments.html", {'form':form})
    except:
        return render(request, 'make_booking.html',{'form':BookingForm()})
