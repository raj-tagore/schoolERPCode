# Generated by Django 5.1.2 on 2024-12-13 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('allocation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='class_teacher',
            field=models.ForeignKey(limit_choices_to={'groups__name': 'Teacher'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='classrooms_leading', to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='other_teachers',
            field=models.ManyToManyField(blank=True, limit_choices_to={'groups__name': 'Teacher'}, related_name='classrooms_assisting', to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='students',
            field=models.ManyToManyField(blank=True, limit_choices_to={'groups__name': 'Student'}, related_name='classrooms', to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='additional_students',
            field=models.ManyToManyField(blank=True, limit_choices_to={'groups__name': 'Student'}, related_name='subjects', to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='main_teacher',
            field=models.ForeignKey(limit_choices_to={'groups__name': 'Teacher'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subjects_leading', to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='other_teachers',
            field=models.ManyToManyField(blank=True, limit_choices_to={'groups__name': 'Teacher'}, related_name='subjects_assisting', to='accounts.account'),
        ),
    ]
