# Generated by Django 5.1.4 on 2024-12-05 23:52

import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BrokerageInvestmentConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='Edited At')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('growth_rate', models.FloatField(help_text='Annual growth rate as a percentage', verbose_name='Growth Rate')),
                ('initial_balance', models.FloatField(help_text='Initial balance in the investment account', verbose_name='Initial Balance')),
                ('contribution_strategy', models.CharField(choices=[('fixed', 'Fixed'), ('percentage_of_income', 'Percentage of Income'), ('max', 'Max')], default='fixed', max_length=50, verbose_name='Contribution Strategy')),
                ('contribution_percentage', models.FloatField(blank=True, help_text='Percentage of income contributed annually', null=True, verbose_name='Contribution Percentage')),
                ('contribution_fixed_amount', models.FloatField(blank=True, help_text='Fixed amount contributed annually', null=True, verbose_name='Contribution Fixed Amount')),
                ('creator', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('editor', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='edited_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Editor')),
            ],
            options={
                'verbose_name': 'Brokerage Investment Configuration',
                'verbose_name_plural': 'Brokerage Investment Configurations',
            },
        ),
        migrations.CreateModel(
            name='CashConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='Edited At')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('initial_amount', models.FloatField(help_text='The starting cash amount.', verbose_name='Initial Amount')),
                ('cash_maintenance_strategy', models.CharField(choices=[('fixedCashReserve', 'Fixed Cash Reserve'), ('variableCashReserve', 'Variable Cash Reserve')], max_length=50, verbose_name='Cash Maintenance Strategy')),
                ('reserve_amount', models.FloatField(blank=True, help_text='The fixed cash reserve amount, if applicable.', null=True, verbose_name='Reserve Amount')),
                ('reserve_months', models.PositiveIntegerField(blank=True, help_text='The number of months of cash to maintain in reserve.', null=True, verbose_name='Reserve Months')),
                ('creator', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('editor', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='edited_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Editor')),
            ],
            options={
                'verbose_name': 'Cash Configuration',
                'verbose_name_plural': 'Cash Configurations',
            },
        ),
        migrations.CreateModel(
            name='DebtConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='Edited At')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('principal', models.FloatField(help_text='The total debt amount.', verbose_name='Principal Amount')),
                ('interest_rate', models.FloatField(help_text='Annual interest rate as a percentage.', verbose_name='Interest Rate')),
                ('payment_minimum', models.FloatField(blank=True, help_text='The minimum required payment.', null=True, verbose_name='Minimum Payment')),
                ('payment_strategy', models.CharField(choices=[('fixed', 'Fixed Payment'), ('minimum_payment', 'Minimum Payment'), ('maximum_payment', 'Maximum Payment'), ('percentage_of_debt', 'Percentage of Debt')], max_length=50, verbose_name='Payment Strategy')),
                ('payment_fixed_amount', models.FloatField(blank=True, help_text='The fixed payment amount, if applicable.', null=True, verbose_name='Fixed Payment Amount')),
                ('payment_percentage', models.FloatField(blank=True, help_text='Percentage of debt to pay each period, if applicable.', null=True, verbose_name='Payment Percentage')),
                ('creator', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('editor', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='edited_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Editor')),
            ],
            options={
                'verbose_name': 'Debt Configuration',
                'verbose_name_plural': 'Debt Configurations',
            },
        ),
        migrations.CreateModel(
            name='ExpenseConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='Edited At')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('amount', models.FloatField(help_text='The expense amount.', verbose_name='Amount')),
                ('type', models.CharField(choices=[('Fixed', 'Fixed'), ('Variable', 'Variable')], max_length=50, verbose_name='Expense Type')),
                ('frequency', models.CharField(choices=[('Monthly', 'Monthly'), ('Weekly', 'Weekly'), ('Quarterly', 'Quarterly'), ('Annually', 'Annually'), ('OneTime', 'One Time')], max_length=50, verbose_name='Frequency')),
                ('is_essential', models.BooleanField(default=False, help_text='Whether the expense is essential.', verbose_name='Is Essential')),
                ('is_tax_deductible', models.BooleanField(default=False, help_text='Whether the expense is tax-deductible.', verbose_name='Is Tax Deductible')),
                ('creator', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('editor', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='edited_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Editor')),
            ],
            options={
                'verbose_name': 'Expense Configuration',
                'verbose_name_plural': 'Expense Configurations',
            },
        ),
        migrations.CreateModel(
            name='IncomeConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='Edited At')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('gross_income', models.FloatField(help_text='The total annual gross income.', verbose_name='Gross Income')),
                ('growth_rate', models.FloatField(help_text='Annual growth rate as a percentage.', verbose_name='Growth Rate')),
                ('income_type', models.CharField(choices=[('ordinary', 'Ordinary')], default='ordinary', max_length=50, verbose_name='Income Type')),
                ('creator', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('editor', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='edited_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Editor')),
            ],
            options={
                'verbose_name': 'Income Configuration',
                'verbose_name_plural': 'Income Configurations',
            },
        ),
        migrations.CreateModel(
            name='IraInvestmentConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='Edited At')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('ira_type', models.CharField(choices=[('taxExempt', 'Tax Exempt'), ('taxDeferred', 'Tax Deferred')], max_length=50, verbose_name='IRA Type')),
                ('growth_rate', models.FloatField(help_text='Annual growth rate as a percentage.', verbose_name='Growth Rate')),
                ('initial_balance', models.FloatField(help_text='Initial balance in the IRA account.', verbose_name='Initial Balance')),
                ('contribution_strategy', models.CharField(choices=[('fixed', 'Fixed'), ('percentage_of_income', 'Percentage of Income'), ('max', 'Max')], default='fixed', max_length=50, verbose_name='Contribution Strategy')),
                ('contribution_percentage', models.FloatField(blank=True, help_text='Percentage of income contributed annually.', null=True, verbose_name='Contribution Percentage')),
                ('contribution_fixed_amount', models.FloatField(blank=True, help_text='Fixed amount contributed annually.', null=True, verbose_name='Contribution Fixed Amount')),
                ('creator', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('editor', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='edited_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Editor')),
            ],
            options={
                'verbose_name': 'IRA Investment Configuration',
                'verbose_name_plural': 'IRA Investment Configurations',
            },
        ),
        migrations.CreateModel(
            name='RetirementConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='Edited At')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('life_expectancy', models.PositiveIntegerField(help_text='Estimated life expectancy in years.', verbose_name='Life Expectancy')),
                ('retirement_strategy', models.CharField(choices=[('fixed_withdrawal', 'Fixed Withdrawal'), ('percentage_of_savings', 'Percentage of Savings'), ('other', 'Other')], max_length=50, verbose_name='Retirement Strategy')),
                ('retirement_withdrawal_rate', models.FloatField(help_text='Annual withdrawal rate as a percentage.', verbose_name='Retirement Withdrawal Rate')),
                ('retirement_income_goal', models.FloatField(help_text='Annual income goal during retirement.', verbose_name='Retirement Income Goal')),
                ('retirement_age', models.PositiveIntegerField(help_text='The age at which retirement starts.', verbose_name='Retirement Age')),
                ('retirement_savings_amount', models.FloatField(help_text='Initial savings amount at the time of retirement.', verbose_name='Retirement Savings Amount')),
                ('creator', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('editor', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='edited_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Editor')),
            ],
            options={
                'verbose_name': 'Retirement Configuration',
                'verbose_name_plural': 'Retirement Configurations',
            },
        ),
        migrations.CreateModel(
            name='TaxConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='Edited At')),
                ('tax_strategy', models.CharField(choices=[('simple', 'Simple')], default='simple', max_length=50, verbose_name='Tax Strategy')),
                ('tax_rate', models.FloatField(help_text='Applicable tax rate as a percentage.', verbose_name='Tax Rate')),
                ('creator', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('editor', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='edited_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Editor')),
            ],
            options={
                'verbose_name': 'Tax Configuration',
                'verbose_name_plural': 'Tax Configurations',
            },
        ),
        migrations.CreateModel(
            name='TaxDeferredInvestmentConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='Edited At')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('growth_rate', models.FloatField(help_text='Annual growth rate as a percentage.', verbose_name='Growth Rate')),
                ('initial_balance', models.FloatField(help_text='Initial balance in the tax-deferred investment account.', verbose_name='Initial Balance')),
                ('elective_contribution_strategy', models.CharField(choices=[('none', 'None'), ('until_company_match', 'Until Company Match'), ('percentage_of_income', 'Percentage of Income'), ('fixed', 'Fixed'), ('max', 'Max')], max_length=50, verbose_name='Elective Contribution Strategy')),
                ('elective_contribution_percentage', models.FloatField(blank=True, help_text='Percentage of income contributed annually.', null=True, verbose_name='Elective Contribution Percentage')),
                ('elective_contribution_fixed_amount', models.FloatField(blank=True, help_text='Fixed amount contributed annually.', null=True, verbose_name='Elective Contribution Fixed Amount')),
                ('employer_contributes', models.BooleanField(default=False, help_text='Whether the employer contributes to the account.', verbose_name='Employer Contributes')),
                ('employer_contribution_strategy', models.CharField(blank=True, choices=[('none', 'None'), ('percentage_of_contribution', 'Percentage of Contribution'), ('percentage_of_compensation', 'Percentage of Compensation'), ('fixed', 'Fixed')], max_length=50, null=True, verbose_name='Employer Contribution Strategy')),
                ('employer_compensation_match_percentage', models.FloatField(blank=True, help_text='Percentage of compensation matched by the employer.', null=True, verbose_name='Employer Compensation Match Percentage')),
                ('employer_contribution_fixed_amount', models.FloatField(blank=True, help_text='Fixed amount contributed by the employer annually.', null=True, verbose_name='Employer Contribution Fixed Amount')),
                ('employer_match_percentage', models.FloatField(blank=True, help_text='Percentage of employee contributions matched by the employer.', null=True, verbose_name='Employer Match Percentage')),
                ('employer_match_percentage_limit', models.FloatField(blank=True, help_text='Limit on the percentage of employee contributions matched by the employer.', null=True, verbose_name='Employer Match Percentage Limit')),
                ('creator', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('editor', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='edited_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Editor')),
            ],
            options={
                'verbose_name': 'Tax-Deferred Investment Configuration',
                'verbose_name_plural': 'Tax-Deferred Investment Configurations',
            },
        ),
        migrations.CreateModel(
            name='BrokerageInvestmentTemplate',
            fields=[
                ('brokerageinvestmentconfig_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.brokerageinvestmentconfig')),
                ('template_description', models.TextField(blank=True, help_text='Description of the template for documentation purposes.', null=True, verbose_name='Template Description')),
            ],
            options={
                'verbose_name': 'Brokerage Investment Template',
                'verbose_name_plural': 'Brokerage Investment Templates',
                'db_table': 'brokerage_investment_template',
            },
            bases=('main.brokerageinvestmentconfig',),
        ),
        migrations.CreateModel(
            name='CashTemplate',
            fields=[
                ('cashconfig_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.cashconfig')),
                ('template_description', models.TextField(blank=True, help_text='Description of the template for documentation purposes.', null=True, verbose_name='Template Description')),
            ],
            options={
                'verbose_name': 'Cash Configuration Template',
                'verbose_name_plural': 'Cash Configuration Templates',
                'db_table': 'cash_config_template',
            },
            bases=('main.cashconfig',),
        ),
        migrations.CreateModel(
            name='DebtTemplate',
            fields=[
                ('debtconfig_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.debtconfig')),
                ('template_description', models.TextField(blank=True, help_text='Description of the template for documentation purposes.', null=True, verbose_name='Template Description')),
            ],
            options={
                'verbose_name': 'Debt Configuration Template',
                'verbose_name_plural': 'Debt Configuration Templates',
                'db_table': 'debt_config_template',
            },
            bases=('main.debtconfig',),
        ),
        migrations.CreateModel(
            name='ExpenseTemplate',
            fields=[
                ('expenseconfig_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.expenseconfig')),
                ('template_description', models.TextField(blank=True, help_text='Description of the template for documentation purposes.', null=True, verbose_name='Template Description')),
            ],
            options={
                'verbose_name': 'Expense Configuration Template',
                'verbose_name_plural': 'Expense Configuration Templates',
                'db_table': 'expense_config_template',
            },
            bases=('main.expenseconfig',),
        ),
        migrations.CreateModel(
            name='IncomeTemplate',
            fields=[
                ('incomeconfig_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.incomeconfig')),
                ('template_description', models.TextField(blank=True, help_text='Description of the template for documentation purposes.', null=True, verbose_name='Template Description')),
            ],
            options={
                'verbose_name': 'Income Configuration Template',
                'verbose_name_plural': 'Income Configuration Templates',
                'db_table': 'income_config_template',
            },
            bases=('main.incomeconfig',),
        ),
        migrations.CreateModel(
            name='IraInvestmentTemplate',
            fields=[
                ('irainvestmentconfig_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.irainvestmentconfig')),
                ('template_description', models.TextField(blank=True, help_text='Description of the template for documentation purposes.', null=True, verbose_name='Template Description')),
            ],
            options={
                'verbose_name': 'IRA Investment Configuration Template',
                'verbose_name_plural': 'IRA Investment Configuration Templates',
                'db_table': 'ira_investment_config_template',
            },
            bases=('main.irainvestmentconfig',),
        ),
        migrations.CreateModel(
            name='RetirementTemplate',
            fields=[
                ('retirementconfig_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.retirementconfig')),
                ('template_description', models.TextField(blank=True, help_text='Description of the template for documentation purposes.', null=True, verbose_name='Template Description')),
            ],
            options={
                'verbose_name': 'Retirement Configuration Template',
                'verbose_name_plural': 'Retirement Configuration Templates',
                'db_table': 'retirement_config_template',
            },
            bases=('main.retirementconfig',),
        ),
        migrations.CreateModel(
            name='TaxTemplate',
            fields=[
                ('taxconfig_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.taxconfig')),
                ('template_description', models.TextField(blank=True, help_text='Description of the template for documentation purposes.', null=True, verbose_name='Template Description')),
            ],
            options={
                'verbose_name': 'Tax Configuration Template',
                'verbose_name_plural': 'Tax Configuration Templates',
                'db_table': 'tax_config_template',
            },
            bases=('main.taxconfig',),
        ),
        migrations.CreateModel(
            name='TaxDeferredInvestmentTemplate',
            fields=[
                ('taxdeferredinvestmentconfig_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.taxdeferredinvestmentconfig')),
                ('template_description', models.TextField(blank=True, help_text='Description of the template for documentation purposes.', null=True, verbose_name='Template Description')),
            ],
            options={
                'verbose_name': 'Tax-Deferred Investment Configuration Template',
                'verbose_name_plural': 'Tax-Deferred Investment Configuration Templates',
                'db_table': 'tax_deferred_investment_config_template',
            },
            bases=('main.taxdeferredinvestmentconfig',),
        ),
        migrations.CreateModel(
            name='PlanConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='Edited At')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('age', models.PositiveIntegerField(verbose_name='Age')),
                ('year', models.PositiveIntegerField(verbose_name='Year')),
                ('inflation_rate', models.FloatField(help_text='Annual inflation rate as a percentage.', verbose_name='Inflation Rate')),
                ('allow_negative_disposable_income', models.CharField(choices=[('none', 'None'), ('minimum_only', 'Minimum Only'), ('full', 'Full')], default='none', max_length=50, verbose_name='Allow Negative Disposable Income')),
                ('brokerage_investments', models.ManyToManyField(related_name='plans', to='main.brokerageinvestmentconfig', verbose_name='Brokerage Investment Configurations')),
                ('cash', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='main.cashconfig', verbose_name='Cash Configuration')),
                ('creator', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('debts', models.ManyToManyField(related_name='plans', to='main.debtconfig', verbose_name='Debt Configurations')),
                ('editor', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='edited_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Editor')),
                ('expenses', models.ManyToManyField(related_name='plans', to='main.expenseconfig', verbose_name='Expense Configurations')),
                ('incomes', models.ManyToManyField(related_name='plans', to='main.incomeconfig', verbose_name='Income Configurations')),
                ('ira_investments', models.ManyToManyField(related_name='plans', to='main.irainvestmentconfig', verbose_name='IRA Investment Configurations')),
                ('retirement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='main.retirementconfig', verbose_name='Retirement Configuration')),
                ('tax', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='main.taxconfig', verbose_name='Tax Configuration')),
                ('tax_deferred_investments', models.ManyToManyField(related_name='plans', to='main.taxdeferredinvestmentconfig', verbose_name='Tax-Deferred Investment Configurations')),
            ],
            options={
                'verbose_name': 'Plan Configuration',
                'verbose_name_plural': 'Plan Configurations',
            },
        ),
        migrations.CreateModel(
            name='PlanTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='Edited At')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('age', models.PositiveIntegerField(verbose_name='Age')),
                ('year', models.PositiveIntegerField(verbose_name='Year')),
                ('inflation_rate', models.FloatField(help_text='Annual inflation rate as a percentage.', verbose_name='Inflation Rate')),
                ('allow_negative_disposable_income', models.CharField(choices=[('none', 'None'), ('minimum_only', 'Minimum Only'), ('full', 'Full')], default='none', max_length=50, verbose_name='Allow Negative Disposable Income')),
                ('creator', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('editor', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='edited_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Editor')),
                ('brokerage_investment_templates', models.ManyToManyField(related_name='plan_templates', to='main.brokerageinvestmenttemplate', verbose_name='Brokerage Investment Templates')),
                ('cash_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_templates', to='main.cashtemplate', verbose_name='Cash Template')),
                ('debt_templates', models.ManyToManyField(related_name='plan_templates', to='main.debttemplate', verbose_name='Debt Templates')),
                ('expense_templates', models.ManyToManyField(related_name='plan_templates', to='main.expensetemplate', verbose_name='Expense Templates')),
                ('income_templates', models.ManyToManyField(related_name='plan_templates', to='main.incometemplate', verbose_name='Income Templates')),
                ('ira_investment_templates', models.ManyToManyField(related_name='plan_templates', to='main.irainvestmenttemplate', verbose_name='IRA Investment Templates')),
                ('retirement_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_templates', to='main.retirementtemplate', verbose_name='Retirement Template')),
                ('tax_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_templates', to='main.taxtemplate', verbose_name='Tax Template')),
                ('tax_deferred_investment_templates', models.ManyToManyField(related_name='plan_templates', to='main.taxdeferredinvestmenttemplate', verbose_name='Tax-Deferred Investment Templates')),
            ],
            options={
                'verbose_name': 'Plan Template',
                'verbose_name_plural': 'Plan Templates',
            },
        ),
    ]
