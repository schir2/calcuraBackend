# Generated by Django 5.1.4 on 2024-12-14 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_plan_age_alter_plan_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantemplate',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='plantemplate',
            name='inflation_rate',
            field=models.FloatField(blank=True, help_text='Annual inflation rate as a percentage.', null=True, verbose_name='Inflation Rate'),
        ),
        migrations.AlterField(
            model_name='plantemplate',
            name='year',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Year'),
        ),
    ]