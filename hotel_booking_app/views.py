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
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .forms import AddRoomType
from .forms import AddRoom

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
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('home')
	else:
		return render(request, 'home.html')




def  login_user(request):
    pass


def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')

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


def dashboard(request):
    # return render(request, "dashboard.html")
    hotels = Hotel.objects.all()
    return render(request, 'dashboard.html', {'hotels': hotels})


def booking(request):
    return render(request, "booking.html")


def user(request):
    return render(request, "user.html")
    #
    # users = Guest.objects.all()
    # return render(request, 'user.html', {'users': users})

def contact(request):

    return render(request, "contact.html")


def inventory(request):
    #rooms = Inventory.objects.all().values()
    #template = loader.get_template('inventory.html')
    #context = {
    #'rooms': rooms,
    #}
    if request.method =='POST':
        form = AddRoomType(request.POST)
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
    inventorys = Inventory.objects.all()
    rooms = Room.objects.all()
    roomtypes = RoomType.objects.all()
    return render(request, 'inventory.html', 
    {'inventorys': inventorys, 'rooms': rooms, 'roomtypes': roomtypes, 'form': form,'form2':form2})

def users(request):
    return render(request, "users.html")

def make_booking(request):
    if request.method =='POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            start = form.cleaned_data['start_date']
            end = form.cleaned_data['end_date']
            adults = form.cleaned_data['adults_number']
            children = form.cleaned_data['children_number']
            print(name)
            print(start)
            print(end)
            print(adults)
            print(children)
            booking_request = Booking(booking_check_in = start, booking_check_out = end, booking_number_of_adults = adults, booking_number_of_children = children)
            try:
                booking_request.save()
            except:
                print('booking failed')

            Booking.objects.all().values()
            return HttpResponseRedirect('/payments')
    else:
        form = BookingForm()
        
    return render(request, 'make_booking.html', {'form': form})

def payments(request):
    return render(request, "payments.html")
