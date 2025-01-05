# Generated by Django 5.1.4 on 2025-01-05 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

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
            ],
        ),
        migrations.CreateModel(
            name="ClassroomJoinLinks",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
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
            ],
        ),
    ]
