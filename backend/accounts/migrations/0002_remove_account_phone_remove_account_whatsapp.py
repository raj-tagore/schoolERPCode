# Generated by Django 5.1.2 on 2025-01-01 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='account',
            name='whatsapp',
        ),
    ]
