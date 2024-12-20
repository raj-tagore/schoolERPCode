# Generated by Django 5.1.2 on 2024-12-16 13:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("allocation", "0001_initial"),
        ("attachments", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Announcement",
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
                ("title", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("release_at", models.DateTimeField()),
                ("expiry_at", models.DateTimeField()),
                (
                    "priority",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("low", "Low Priority"),
                            ("medium", "Medium Priority"),
                            ("high", "High  Priority"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "attachments",
                    models.ManyToManyField(
                        blank=True,
                        related_name="announcements",
                        to="attachments.attachment",
                    ),
                ),
                (
                    "classrooms",
                    models.ManyToManyField(
                        blank=True,
                        related_name="announcements",
                        to="allocation.classroom",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="announcements_created",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "signed_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="announcements_signed",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "subjects",
                    models.ManyToManyField(
                        blank=True,
                        related_name="announcements",
                        to="allocation.subject",
                    ),
                ),
            ],
        ),
    ]
