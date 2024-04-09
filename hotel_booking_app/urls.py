 
from django.urls import path 
from . import views 
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [ 
    
    path("", views.home, name="home"), 
    path("dashboard/", views.dashboard, name="dashboard"), 
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path("booking/", views.booking, name="booking"),
    path("user/", views.user, name="user"),
    path("contact/", views.contact, name="contact"),
    path("inventory/", views.inventory, name="inventory"),
    path("users/", views.users, name="users"),
    path("make_booking/", views.make_booking, name="make_booking"),
    path("payments/", views.payments, name="payments"),
    path("addroomtype/", views.inventory, name="inventory"),
    path("addroom/", views.add_room, name='inventory'),
    path("payment/", views.payments, name='payments')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
