# Generated by Django 4.2.4 on 2023-09-19 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brhindApp', '0010_rename_flight_1_flight_country_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='flight_destinacion',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='flight_destinacion2',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
