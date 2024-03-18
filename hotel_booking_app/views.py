from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#from .models import Inventory

# Create your views here.
def dashboard(request):
    return render(request, "dashboard.html")


def booking(request):
    return render(request, "booking.html")


def user(request):
    return render(request, "user.html")


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
