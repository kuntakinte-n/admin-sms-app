# Generated by Django 4.0.4 on 2022-06-04 22:29

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sms',
            name='number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]