# Generated by Django 5.1.2 on 2025-01-03 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_student_division_remove_student_standard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='occupation',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='office_address',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='whatsapp',
        ),
        migrations.RemoveField(
            model_name='student',
            name='aadhar_card_no',
        ),
        migrations.RemoveField(
            model_name='student',
            name='address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='medical_info',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='qualifications',
        ),
    ]
