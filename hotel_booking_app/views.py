from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, "dashboard.html")


def booking(request):
    return render(request, "booking.html")


def users(request):
    return render(request, "users.html")


def contacts(request):
  return render(request, "contact.html")
