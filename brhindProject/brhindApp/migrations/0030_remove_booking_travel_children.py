# Generated by Django 4.2.4 on 2023-10-01 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brhindApp', '0029_booking_ticket_is_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='travel_children',
        ),
    ]