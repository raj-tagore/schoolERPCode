# Generated by Django 5.1.4 on 2025-01-05 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Parent",
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
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=20, verbose_name="Phone number"
                    ),
                ),
                (
                    "whatsapp",
                    models.CharField(
                        blank=True, max_length=20, verbose_name="WhatsApp number"
                    ),
                ),
                (
                    "occupation",
                    models.CharField(
                        blank=True, max_length=400, verbose_name="Occupation"
                    ),
                ),
                ("office_address", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("student_no", models.CharField(max_length=50, unique=True)),
                ("roll_no", models.CharField(blank=True, max_length=50, null=True)),
                ("standard", models.CharField(blank=True, max_length=50, null=True)),
                ("division", models.CharField(blank=True, max_length=10, null=True)),
                ("address", models.TextField(blank=True, null=True)),
                (
                    "aadhar_card_no",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("medical_info", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Teacher",
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
                ("identifier", models.BigIntegerField(verbose_name="ID")),
                (
                    "qualifications",
                    models.TextField(blank=True, verbose_name="Qualifications"),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=20, verbose_name="Phone number"
                    ),
                ),
                (
                    "whatsapp",
                    models.CharField(
                        blank=True, max_length=20, verbose_name="WhatsApp number"
                    ),
                ),
            ],
        ),
    ]
