# Generated by Django 4.2.4 on 2023-09-27 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brhindApp', '0025_alter_flight_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
