# Generated by Django 4.2.4 on 2023-09-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brhindApp', '0027_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
