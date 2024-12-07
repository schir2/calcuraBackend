# Generated by Django 5.1.4 on 2024-12-08 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='retirementtemplate',
            name='retirementconfig_ptr',
        ),
        migrations.RemoveField(
            model_name='planconfig',
            name='retirement',
        ),
        migrations.RemoveField(
            model_name='plantemplate',
            name='retirement_template',
        ),
        migrations.RemoveField(
            model_name='taxconfig',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='taxconfig',
            name='editor',
        ),
        migrations.RemoveField(
            model_name='taxtemplate',
            name='taxconfig_ptr',
        ),
        migrations.RemoveField(
            model_name='planconfig',
            name='tax',
        ),
        migrations.RemoveField(
            model_name='plantemplate',
            name='tax_template',
        ),
        migrations.AddField(
            model_name='planconfig',
            name='life_expectancy',
            field=models.PositiveIntegerField(default=85, help_text='Estimated life expectancy in years.', verbose_name='Life Expectancy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planconfig',
            name='retirement_age',
            field=models.PositiveIntegerField(default=65, help_text='The age at which retirement starts.', verbose_name='Retirement Age'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planconfig',
            name='retirement_income_goal',
            field=models.FloatField(default=0, help_text='Annual income goal during retirement.', verbose_name='Retirement Income Goal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planconfig',
            name='retirement_savings_amount',
            field=models.FloatField(default=0, help_text='Initial savings amount at the time of retirement.', verbose_name='Retirement Savings Amount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planconfig',
            name='retirement_strategy',
            field=models.CharField(choices=[('fixed_withdrawal', 'Fixed Withdrawal'), ('percentage_of_savings', 'Percentage of Savings'), ('other', 'Other')], default='age', max_length=50, verbose_name='Retirement Strategy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planconfig',
            name='retirement_withdrawal_rate',
            field=models.FloatField(default=0, help_text='Annual withdrawal rate as a percentage.', verbose_name='Retirement Withdrawal Rate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planconfig',
            name='tax_rate',
            field=models.FloatField(default=2.5, help_text='Applicable tax rate as a percentage.', verbose_name='Tax Rate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planconfig',
            name='tax_strategy',
            field=models.CharField(choices=[('simple', 'Simple')], default='simple', max_length=50, verbose_name='Tax Strategy'),
        ),
        migrations.DeleteModel(
            name='RetirementConfig',
        ),
        migrations.DeleteModel(
            name='RetirementTemplate',
        ),
        migrations.DeleteModel(
            name='TaxConfig',
        ),
        migrations.DeleteModel(
            name='TaxTemplate',
        ),
    ]
