# Generated by Django 4.2.4 on 2023-10-08 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brhindApp', '0033_booking_travel_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]