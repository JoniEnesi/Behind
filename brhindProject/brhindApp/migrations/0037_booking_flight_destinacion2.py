# Generated by Django 4.2.4 on 2023-10-09 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brhindApp', '0036_remove_booking_travel_category_booking_travel_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='flight_destinacion2',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]