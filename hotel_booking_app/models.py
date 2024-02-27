from django.db import models


class User(models.Model):
    user_type = models.QuerySet('Admin', 'Reception', 'Stuff', 'Guest')
    user_contact = models.EmailField()


class Room(models.Model):
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50)
    room_cost = models.CharField(max_length=15)

    def __str__(self):
        return self.room_number


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f"{self.guest_name} - {self.room.room_number}"


class Inventory(models.Model):
    rooms_available = models.CharField(max_length=10)
    rooms_in_use = models.CharField(max_length=10)
    rooms_to_be_cleaned = models.CharField(max_length=10)

# class CustomerCommunication(models.Model):
