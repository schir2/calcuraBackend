# Generated by Django 5.1.4 on 2025-03-09 02:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_managers_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2025, 3, 9, 2, 2, 50, 184891, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='life_expectancy',
            field=models.IntegerField(default=0),
        ),
    ]
