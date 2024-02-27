from django.contrib import admin
from .models import Room, Booking, Inventory, User

admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Inventory)
admin.site.register(User)
