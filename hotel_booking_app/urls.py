 
from django.urls import path 
from . import views 
  
urlpatterns = [ 
    path("", views.dashboard, name="dashboard"), 
    path("booking/", views.booking, name="booking"),
    path("user/", views.user, name="user")
    path("contact/", views.contact, name="contact"), 
]
