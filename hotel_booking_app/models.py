from django.db import models
from django.utils import timezone


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=50, primary_key=True)
    hotel_address = models.CharField(max_length=50)
    hotel_city = models.CharField(max_length=50)
    hotel_country = models.CharField(max_length=50)
    hotel_postcode = models.CharField(max_length=50)
    hotel_phone_number = models.CharField(max_length=20)
    hotel_star_rating = models.CharField(max_length=10)

    class Meta:
        db_table = 'hotel'

    def __str__(self):
        return self.hotel_name


class EmployeeRole(models.Model):
    employee_role_id = models.CharField(max_length=50, primary_key=True)
    employee_role_title = models.CharField(max_length=50)
    employee_role_description = models.TextField()

    class Meta:
        db_table = 'roles'

    def __str__(self):
        return self.employee_role_title


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_last_name = models.CharField(max_length=50)
    employee_first_name = models.CharField(max_length=50)
    employee_date_of_birth = models.DateField()
    employee_gender = models.CharField(max_length=10)
    employee_phone = models.CharField(max_length=20)
    employee_email = models.EmailField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    roles = models.ManyToManyField(EmployeeRole, related_name='employees')

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return (f"Employee Name:{self.employee_first_name} {self.employee_last_name}, "
                f"Employee Role ID:{EmployeeRole.employee_role_id}")


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    booking_made_date_time = models.DateTimeField(default=timezone.now)
    booking_check_in = models.DateTimeField(default=timezone.now)
    booking_check_out = models.DateTimeField(default=timezone.now)
    booking_number_of_adults = models.IntegerField()
    booking_number_of_children = models.IntegerField()
    booking_special_requests = models.TextField()
    guest = models.ForeignKey('Guest', on_delete=models.CASCADE, related_name='guest_bookings', null=True, blank=True)
    room = models.ForeignKey('Room', on_delete=models.CASCADE, related_name='room_bookings', null=True, blank=True)
    payment = models.ForeignKey('Payment', on_delete=models.CASCADE, related_name='payment_bookings', null=True,
                                blank=True)

    class Meta:
        db_table = 'booking'

    def __str__(self):
        return (f"Booking ID:{self.booking_id}, Check-in:{self.booking_check_in}, Check-out:{self.booking_check_out}"
                f"Guest ID:{self.guest_id}, Room ID:{self.room_id}")


class Guest(models.Model):
    guest_id = models.AutoField(primary_key=True)
    guest_title = models.CharField(max_length=10)
    guest_first_name = models.CharField(max_length=50)
    guest_last_name = models.CharField(max_length=50)
    guest_date_of_birth = models.DateField(default=timezone.now)
    guest_phone_number = models.CharField(max_length=20)
    guest_email = models.EmailField()
    guest_address = models.CharField(max_length=50)
    guest_city = models.CharField(max_length=50)
    guest_state = models.CharField(max_length=50)
    guest_country = models.CharField(max_length=50)
    guest_postcode = models.CharField(max_length=10)
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE, related_name='guest_booking', null=True,
                                blank=True)
    payment = models.ForeignKey('Payment', on_delete=models.CASCADE, related_name='guest_payment', null=True,
                                blank=True)

    class Meta:
        db_table = 'guest'

    def __str__(self):
        return (f"Guest ID:{self.guest_id}, Name:{self.guest_title} {self.guest_first_name} {self.guest_last_name},  "
                f"Booking ID:{self.booking_id}")


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length=20)
    room_status = models.CharField(max_length=20)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.ForeignKey('RoomType', on_delete=models.CASCADE)

    class Meta:
        db_table = 'room'

    def __str__(self):
        return f"Room Id:{self.room_id}, Room Status:{self.room_status}"


class RoomType(models.Model):
    room_type_name = models.CharField(max_length=50, primary_key=True)
    room_type_description = models.TextField()
    room_type_images = models.ImageField(upload_to='media/images', null=True, blank=True)
    room_type_price = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        db_table = 'room_type'

    def __str__(self):
        return (f"Room Type:{self.room_type_name}, Description:{self.room_type_description}, "
                f"Description:{self.room_type_images}, Description:{self.room_type_price}")


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_date = models.DateField(default=timezone.now)
    payment_card_number = models.TextField()
    payment_card_expiry_date = models.DateField()
    payment_for_booking = models.DecimalField(max_digits=20, decimal_places=2)
    payment_for_service = models.DecimalField(max_digits=20, decimal_places=2)
    payment_for_bar = models.DecimalField(max_digits=20, decimal_places=2)
    payment_for_late_check_out = models.DecimalField(max_digits=20, decimal_places=2)
    payment_for_miscellaneous = models.DecimalField(max_digits=20, decimal_places=2)
    payment_for_miscellaneous_description = models.TextField()
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE, related_name='payment_booking', null=True,
                                blank=True)
    guest = models.ForeignKey('Guest', on_delete=models.CASCADE, related_name='payment_guest', null=True, blank=True)

    class Meta:
        db_table = 'payment'

    def __str__(self):
        return (f"Payment ID:{self.payment_id}, Date:{self.payment_date}, Booking ID:{self.booking_id}, "
                f"Guest ID:{self.guest_id}")


class Inventory(models.Model):
    inventory_status = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE, default=None)
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE, related_name='inventory_booking', default=None)
    guest = models.ForeignKey('Guest', on_delete=models.CASCADE, related_name='inventory_guest', default=None)

    class Meta:
        db_table = 'inventory'  # changed from 'room' to 'inventory'

    def __str__(self):
        return (f"Inventory_status:{self.inventory_status}, Room Number:{self.room_id}, Guest ID:{self.guest_id}, "
                f"Booking ID:{self.inventory_status}")
