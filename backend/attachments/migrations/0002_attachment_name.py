# Generated by Django 5.1.2 on 2024-12-10 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='Name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
