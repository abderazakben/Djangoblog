# Generated by Django 3.1.7 on 2021-04-07 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apphotil', '0002_hotel_hour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='quantity',
        ),
    ]