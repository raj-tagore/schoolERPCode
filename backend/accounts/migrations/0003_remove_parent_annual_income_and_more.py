# Generated by Django 5.1.2 on 2025-01-02 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='annual_income',
        ),
        migrations.RemoveField(
            model_name='student',
            name='birth_place',
        ),
        migrations.RemoveField(
            model_name='student',
            name='caste',
        ),
        migrations.RemoveField(
            model_name='student',
            name='mother_tongue',
        ),
        migrations.RemoveField(
            model_name='student',
            name='nationality',
        ),
        migrations.RemoveField(
            model_name='student',
            name='religion',
        ),
    ]
