from django.shortcuts import render


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
    return render(request, "inventory.html")
