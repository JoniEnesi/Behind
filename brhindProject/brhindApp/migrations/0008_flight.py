# Generated by Django 4.2.4 on 2023-09-18 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brhindApp', '0007_remove_booking_travel_oneway'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flight_id', models.AutoField(primary_key=True, serialize=False)),
                ('flight_1', models.CharField(blank=True, max_length=60, null=True)),
                ('flight_2', models.CharField(blank=True, max_length=60, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
