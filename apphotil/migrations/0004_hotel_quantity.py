# Generated by Django 3.1.7 on 2021-04-07 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apphotil', '0003_remove_hotel_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='quantity',
            field=models.CharField(blank=True, choices=[('Hour', '1000'), ('date', '100')], max_length=200, null=True),
        ),
    ]
