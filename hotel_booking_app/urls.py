 
from django.urls import path 
from . import views 
  
urlpatterns = [ 
    path("", views.dashboard, name="dashboard"), 
    path("booking/", views.booking, name="booking"),
    path("user/", views.user, name="user"),
    path("contact/", views.contact, name="contact"),
    path("inventory/", views.inventory, name="inventory"),
    path("users/", views.users, name="users"),
    path("makebooking/", views.make_booking, name="make_booking"),
    path("payments/", views.payments, name="payments")
]
