# Generated by Django 5.1.4 on 2025-01-12 04:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_remove_taxdeferredinvestment_income'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxdeferredinvestment',
            name='income',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.income', verbose_name='Income'),
        ),
    ]