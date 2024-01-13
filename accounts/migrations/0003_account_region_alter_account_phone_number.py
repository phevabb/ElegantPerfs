# Generated by Django 5.0.1 on 2024-01-13 17:09

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_is_superadmin_account_is_superuser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='region',
            field=models.CharField(blank=True, choices=[('AR', 'Ashanti Region'), ('BA', 'Brong-Ahafo Region'), ('CR', 'Central Region'), ('ER', 'Eastern Region'), ('NR', 'Northern Region'), ('UE', 'Upper East Region'), ('UW', 'Upper West Region'), ('VR', 'Volta Region'), ('WR', 'Western Region'), ('GR', 'Greater Accra Region')], max_length=2),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
