from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, "dashboard.html")


def booking(request):
    return render(request, "booking.html")


def user(request):
    return render(request, "user.html")


def contacts(request):
  return render(request, "contact.html")
