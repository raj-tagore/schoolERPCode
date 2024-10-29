# Generated by Django 5.1.2 on 2024-10-29 05:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('allocation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('record', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('L', 'Late'), ('E', 'Excused')], max_length=50)),
                ('classroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attendances', to='allocation.classroom')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='accounts.student')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attendances', to='allocation.subject')),
            ],
        ),
    ]
