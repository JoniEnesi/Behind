# Generated by Django 4.2.4 on 2023-09-20 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brhindApp', '0018_flight1_remove_flight_price2_remove_flight_time2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight1',
            name='price',
        ),
        migrations.RemoveField(
            model_name='flight1',
            name='time',
        ),
        migrations.RemoveField(
            model_name='flight1',
            name='time_1',
        ),
    ]
