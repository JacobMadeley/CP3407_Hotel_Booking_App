from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def dashboard(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render())
    # return render(request, "dashboard.html")


def booking(request):
    return render(request, "booking.html")


def user(request):
    return render(request, "user.html")


def contact(request):
  return render(request, "contact.html")
