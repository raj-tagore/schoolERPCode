# Generated by Django 5.1.2 on 2024-12-14 15:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('allocation', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('release_date', models.DateTimeField()),
                ('expiry_date', models.DateTimeField()),
                ('priority', models.CharField(blank=True, choices=[('low', 'Low Priority'), ('medium', 'Medium Priority'), ('high', 'High  Priority')], max_length=10, null=True)),
                ('classrooms', models.ManyToManyField(blank=True, related_name='announcements', to='allocation.classroom')),
                ('signed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('subjects', models.ManyToManyField(blank=True, related_name='announcements', to='allocation.subject')),
            ],
        ),
    ]
