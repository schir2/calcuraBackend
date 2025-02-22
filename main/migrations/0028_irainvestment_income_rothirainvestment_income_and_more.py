# Generated by Django 5.1.4 on 2025-01-12 04:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_alter_plan_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='irainvestment',
            name='income',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.income', verbose_name='Income'),
        ),
        migrations.AddField(
            model_name='rothirainvestment',
            name='income',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.income', verbose_name='Income'),
        ),
        migrations.AlterField(
            model_name='taxdeferredinvestment',
            name='income',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.income', verbose_name='Income'),
        ),
    ]
