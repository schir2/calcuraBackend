# Generated by Django 5.1.4 on 2024-12-08 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_planconfig_retirement_strategy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planconfig',
            old_name='cash',
            new_name='cashes',
        ),
    ]
