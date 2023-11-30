# Generated by Django 4.2.7 on 2023-11-30 08:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kinozal', '0011_alter_userpreferences_last_scan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreferences',
            name='last_scan',
            field=models.DateField(default=datetime.datetime(2023, 6, 3, 10, 23, 27, 558215)),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='preferences', to=settings.AUTH_USER_MODEL),
        ),
    ]