# Generated by Django 5.1.2 on 2024-10-31 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_student_user_remove_teacher_user_and_more'),
        ('allocation', '0002_alter_classroom_class_teacher_and_more'),
        ('announcements', '0002_alter_announcement_signed_by'),
        ('assessments', '0002_alter_studentassessment_student'),
        ('assignments', '0002_alter_studentassignment_student'),
        ('attendance', '0002_alter_attendance_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
