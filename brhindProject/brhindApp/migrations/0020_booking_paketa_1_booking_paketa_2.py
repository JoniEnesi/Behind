# Generated by Django 4.2.4 on 2023-09-20 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brhindApp', '0019_remove_flight1_price_remove_flight1_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='Paketa_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='Paketa_2',
            field=models.BooleanField(default=False),
        ),
    ]