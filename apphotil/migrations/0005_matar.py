# Generated by Django 3.1.7 on 2021-04-10 23:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apphotil', '0004_hotel_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cars', models.CharField(blank=True, choices=[('Vito', '350'), ('E220', '500'), ('Santafi', '300')], max_length=200, null=True)),
                ('date_activiti', models.DateTimeField(auto_now_add=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
