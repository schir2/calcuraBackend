# Generated by Django 5.1.4 on 2024-12-16 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_rename_type_expense_expense_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='growth_rate',
            field=models.FloatField(default=0, help_text='The growth rate.', verbose_name='Growth Rate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expensetemplate',
            name='growth_rate',
            field=models.FloatField(default=0, help_text='The growth rate.', verbose_name='Growth Rate'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='expense',
            name='frequency',
            field=models.CharField(choices=[('monthly', 'Monthly'), ('weekly', 'Weekly'), ('biweekly', 'Biweekly'), ('quarterly', 'Quarterly'), ('annual', 'Annually'), ('one_time', 'One Time')], max_length=50, verbose_name='Frequency'),
        ),
        migrations.AlterField(
            model_name='expensetemplate',
            name='frequency',
            field=models.CharField(choices=[('monthly', 'Monthly'), ('weekly', 'Weekly'), ('biweekly', 'Biweekly'), ('quarterly', 'Quarterly'), ('annual', 'Annually'), ('one_time', 'One Time')], max_length=50, verbose_name='Frequency'),
        ),
    ]
