from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .forms import BookingForm
from .models import Guest
from .models import Hotel

# Create your views here.
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
    return render(request, "inventory.html")
    #return HttpResponse(template.render(context, request))

def users(request):
    return render(request, "users.html")

def make_booking(request):
    if request.method =='POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            start = form.cleaned_data['start_date']
            end = form.cleaned_data['end_date']
            print(name)
            print(start)
            print(end)
            return HttpResponseRedirect('/')
    else:
        form = BookingForm()
        
    return render(request, 'make_booking.html', {'form': form})

def payments(request):
    return render(request, "payments.html")
