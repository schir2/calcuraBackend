# Generated by Django 5.1.4 on 2024-12-13 19:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_template_description_brokerageinvestmenttemplate_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantemplate',
            name='brokerage_investment_templates',
            field=models.ManyToManyField(blank=True, related_name='plan_templates', to='main.brokerageinvestmenttemplate', verbose_name='Brokerage Investment Templates'),
        ),
        migrations.AlterField(
            model_name='plantemplate',
            name='cash_reserve_templates',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plan_templates', to='main.cashreservetemplate', verbose_name='Cash Template'),
        ),
        migrations.AlterField(
            model_name='plantemplate',
            name='debt_templates',
            field=models.ManyToManyField(blank=True, related_name='plan_templates', to='main.debttemplate', verbose_name='Debt Templates'),
        ),
        migrations.AlterField(
            model_name='plantemplate',
            name='expense_templates',
            field=models.ManyToManyField(blank=True, related_name='plan_templates', to='main.expensetemplate', verbose_name='Expense Templates'),
        ),
        migrations.AlterField(
            model_name='plantemplate',
            name='income_templates',
            field=models.ManyToManyField(blank=True, related_name='plan_templates', to='main.incometemplate', verbose_name='Income Templates'),
        ),
        migrations.AlterField(
            model_name='plantemplate',
            name='ira_investment_templates',
            field=models.ManyToManyField(blank=True, related_name='plan_templates', to='main.irainvestmenttemplate', verbose_name='IRA Investment Templates'),
        ),
        migrations.AlterField(
            model_name='plantemplate',
            name='tax_deferred_investment_templates',
            field=models.ManyToManyField(blank=True, related_name='plan_templates', to='main.taxdeferredinvestmenttemplate', verbose_name='Tax-Deferred Investment Templates'),
        ),
    ]
