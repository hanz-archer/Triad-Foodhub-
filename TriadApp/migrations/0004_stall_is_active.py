# Generated by Django 5.1.4 on 2025-01-14 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TriadApp', '0003_rename_admin_adminprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='stall',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]