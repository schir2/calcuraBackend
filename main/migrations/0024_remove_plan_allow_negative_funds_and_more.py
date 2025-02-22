# Generated by Django 5.1.4 on 2024-12-19 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_remove_plan_allow_negative_disposable_income_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='allow_negative_funds',
        ),
        migrations.RemoveField(
            model_name='plantemplate',
            name='allow_negative_funds',
        ),
        migrations.AddField(
            model_name='plan',
            name='insufficient_funds_strategy',
            field=models.CharField(choices=[('none', 'None'), ('minimum_only', 'Minimum Only'), ('full', 'Full')], default='none', max_length=50, verbose_name='Insufficient Funds Strategy'),
        ),
        migrations.AddField(
            model_name='plantemplate',
            name='insufficient_funds_strategy',
            field=models.CharField(choices=[('none', 'None'), ('minimum_only', 'Minimum Only'), ('full', 'Full')], default='none', max_length=50, verbose_name='Insufficient Funds Strategy'),
        ),
    ]
