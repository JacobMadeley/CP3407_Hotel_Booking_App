# Generated by Django 4.2.10 on 2024-04-08 08:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('booking_made_date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('booking_check_in', models.DateTimeField(default=django.utils.timezone.now)),
                ('booking_check_out', models.DateTimeField(default=django.utils.timezone.now)),
                ('booking_number_of_adults', models.IntegerField()),
                ('booking_number_of_children', models.IntegerField()),
                ('booking_special_requests', models.TextField()),
            ],
            options={
                'db_table': 'booking',
            },
        ),
        migrations.CreateModel(
            name='EmployeeRole',
            fields=[
                ('employee_role_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('employee_role_title', models.CharField(max_length=50)),
                ('employee_role_description', models.TextField()),
            ],
            options={
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('guest_id', models.AutoField(primary_key=True, serialize=False)),
                ('guest_title', models.CharField(max_length=10)),
                ('guest_first_name', models.CharField(max_length=50)),
                ('guest_last_name', models.CharField(max_length=50)),
                ('guest_date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('guest_phone_number', models.CharField(max_length=20)),
                ('guest_email', models.EmailField(max_length=254)),
                ('guest_address', models.CharField(max_length=50)),
                ('guest_city', models.CharField(max_length=50)),
                ('guest_state', models.CharField(max_length=50)),
                ('guest_country', models.CharField(max_length=50)),
                ('guest_postcode', models.CharField(max_length=10)),
                ('booking', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guest_booking', to='hotel_booking_app.booking')),
            ],
            options={
                'db_table': 'guest',
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('hotel_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('hotel_address', models.CharField(max_length=50)),
                ('hotel_city', models.CharField(max_length=50)),
                ('hotel_country', models.CharField(max_length=50)),
                ('hotel_postcode', models.CharField(max_length=50)),
                ('hotel_phone_number', models.CharField(max_length=20)),
                ('hotel_star_rating', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'hotel',
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('room_type_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('room_type_description', models.TextField()),
                ('room_type_images', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('room_type_price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
            options={
                'db_table': 'room_type',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('room_number', models.CharField(max_length=20)),
                ('room_status', models.CharField(max_length=20)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_booking_app.hotel')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_booking_app.roomtype')),
            ],
            options={
                'db_table': 'room',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_date', models.DateField(default=django.utils.timezone.now)),
                ('payment_card_number', models.TextField()),
                ('payment_card_expiry_date', models.DateField()),
                ('payment_for_booking', models.DecimalField(decimal_places=2, max_digits=20)),
                ('payment_for_service', models.DecimalField(decimal_places=2, max_digits=20)),
                ('payment_for_bar', models.DecimalField(decimal_places=2, max_digits=20)),
                ('payment_for_late_check_out', models.DecimalField(decimal_places=2, max_digits=20)),
                ('payment_for_miscellaneous', models.DecimalField(decimal_places=2, max_digits=20)),
                ('payment_for_miscellaneous_description', models.TextField()),
                ('booking', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment_booking', to='hotel_booking_app.booking')),
                ('guest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment_guest', to='hotel_booking_app.guest')),
            ],
            options={
                'db_table': 'payment',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('inventory_status', models.AutoField(primary_key=True, serialize=False)),
                ('booking', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='inventory_booking', to='hotel_booking_app.booking')),
                ('guest', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='inventory_guest', to='hotel_booking_app.guest')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_booking_app.hotel')),
                ('room', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hotel_booking_app.room')),
            ],
            options={
                'db_table': 'inventory',
            },
        ),
        migrations.AddField(
            model_name='guest',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guest_payment', to='hotel_booking_app.payment'),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_last_name', models.CharField(max_length=50)),
                ('employee_first_name', models.CharField(max_length=50)),
                ('employee_date_of_birth', models.DateField()),
                ('employee_gender', models.CharField(max_length=10)),
                ('employee_phone', models.CharField(max_length=20)),
                ('employee_email', models.EmailField(max_length=254)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_booking_app.hotel')),
                ('roles', models.ManyToManyField(related_name='employees', to='hotel_booking_app.employeerole')),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.AddField(
            model_name='booking',
            name='guest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guest_bookings', to='hotel_booking_app.guest'),
        ),
        migrations.AddField(
            model_name='booking',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment_bookings', to='hotel_booking_app.payment'),
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_bookings', to='hotel_booking_app.room'),
        ),
    ]
