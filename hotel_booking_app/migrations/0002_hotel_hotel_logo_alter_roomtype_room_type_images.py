# Generated by Django 5.0.4 on 2024-04-11 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_booking_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='hotel_logo',
            field=models.ImageField(blank=True, null=True, upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='room_type_images',
            field=models.ImageField(blank=True, null=True, upload_to='media/images'),
        ),
    ]