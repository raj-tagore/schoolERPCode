# Generated by Django 5.1.4 on 2025-01-06 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Classroom",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("is_active", models.BooleanField(default=True)),
                ("standard", models.CharField(max_length=50)),
                (
                    "class_teacher",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="classrooms_leading",
                        to="accounts.teacher",
                    ),
                ),
                (
                    "other_teachers",
                    models.ManyToManyField(
                        blank=True,
                        related_name="classrooms_assisting",
                        to="accounts.teacher",
                    ),
                ),
                (
                    "students",
                    models.ManyToManyField(
                        blank=True, related_name="classrooms", to="accounts.student"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("is_active", models.BooleanField(default=True)),
                ("description", models.TextField()),
                (
                    "classroom",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="subjects",
                        to="allocation.classroom",
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="subjects",
                        to="accounts.teacher",
                    ),
                ),
            ],
        ),
    ]
