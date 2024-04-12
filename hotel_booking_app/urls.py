from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

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
                  path("add_room_type/", views.inventory, name="inventory"),
                  path("add_room/", views.add_room, name='inventory'),
                  path("payment/", views.payments, name='payments'),
                  path('add_record/', views.add_record, name='add_record'),
                  path('updatestatus/', views.updatestatus,name='updatestatus')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Path: hotel_booking_app/views.py
