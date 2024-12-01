# Generated by Django 5.1.2 on 2024-11-30 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_account_address_alter_account_first_name_and_more'),
        ('allocation', '0002_alter_classroom_class_teacher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='class_teacher',
            field=models.ForeignKey(limit_choices_to={'group': 'Teacher'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='classrooms_leading', to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='other_teachers',
            field=models.ManyToManyField(limit_choices_to={'group': 'Student'}, related_name='classrooms_assisting', to='accounts.account'),
        ),
    ]
