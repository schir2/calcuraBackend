# Generated by Django 5.1.4 on 2025-01-08 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_plan_roth_ira_investments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='year',
            field=models.PositiveIntegerField(blank=True, default=2025, null=True, verbose_name='Year'),
        ),
    ]