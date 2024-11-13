# Generated by Django 5.1.2 on 2024-10-31 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_account_groups_account_is_superuser_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
        migrations.AddField(
            model_name='account',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='standard',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]
