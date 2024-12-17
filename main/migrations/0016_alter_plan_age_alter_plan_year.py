# Generated by Django 5.1.4 on 2024-12-14 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_expense_frequency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='age',
            field=models.PositiveIntegerField(default=30, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='year',
            field=models.PositiveIntegerField(default=2024, verbose_name='Year'),
        ),
    ]