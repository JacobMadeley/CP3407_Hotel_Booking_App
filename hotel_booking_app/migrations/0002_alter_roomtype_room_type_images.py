# Generated by Django 5.0.4 on 2024-04-05 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_booking_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomtype',
            name='room_type_images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
