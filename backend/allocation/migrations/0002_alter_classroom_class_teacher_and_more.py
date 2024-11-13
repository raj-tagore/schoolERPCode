# Generated by Django 5.1.2 on 2024-10-31 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_student_user_remove_teacher_user_and_more'),
        ('allocation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='class_teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='classrooms_leading', to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='other_teachers',
            field=models.ManyToManyField(related_name='classrooms_assisting', to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='students',
            field=models.ManyToManyField(limit_choices_to={'group': 'Student'}, related_name='classrooms', to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='additional_students',
            field=models.ManyToManyField(related_name='subjects', to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='main_teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subjects_leading', to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='other_teachers',
            field=models.ManyToManyField(related_name='subjects_assisting', to='accounts.account'),
        ),
    ]
