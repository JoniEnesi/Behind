# Generated by Django 4.2.4 on 2023-10-08 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brhindApp', '0035_remove_booking_travel_city_booking_travel_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='travel_category',
        ),
        migrations.AddField(
            model_name='booking',
            name='travel_city',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
