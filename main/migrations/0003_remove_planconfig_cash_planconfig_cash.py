# Generated by Django 5.1.4 on 2024-12-08 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_retirementtemplate_retirementconfig_ptr_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planconfig',
            name='cash',
        ),
        migrations.AddField(
            model_name='planconfig',
            name='cash',
            field=models.ManyToManyField(related_name='plans', to='main.cashconfig', verbose_name='Cash Configuration'),
        ),
    ]