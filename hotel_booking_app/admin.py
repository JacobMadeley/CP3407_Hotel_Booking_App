from django.contrib import admin
from .models import Hotel, EmployeeRole, Employee, Booking, Guest, Room, RoomType, Payment

admin.site.register(Hotel)
admin.site.register(EmployeeRole)
admin.site.register(Employee)
admin.site.register(Booking)
admin.site.register(Guest)
admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(Payment)
