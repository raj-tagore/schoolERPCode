# Generated by Django 5.1.2 on 2025-01-02 23:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_remove_parent_annual_income_and_more'),
        ('allocation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('syllabus', models.TextField()),
                ('datetime', models.DateTimeField()),
                ('venue', models.CharField(max_length=50)),
                ('max_marks', models.IntegerField()),
                ('passing_marks', models.IntegerField()),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assessments', to='allocation.subject')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='assessments.assessment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessments', to='accounts.student')),
            ],
        ),
    ]
