from django.contrib import admin

from .models import BrokerageInvestmentConfig, BrokerageInvestmentTemplate, CashConfig, CashTemplate, DebtConfig, \
    DebtTemplate, ExpenseTemplate, IncomeConfig, IncomeTemplate, IraInvestmentTemplate, \
    IraInvestmentConfig, ExpenseConfig, RetirementConfig, RetirementTemplate, TaxTemplate, TaxConfig, \
    TaxDeferredInvestmentTemplate, TaxDeferredInvestmentConfig, PlanConfig, PlanTemplate


@admin.register(BrokerageInvestmentConfig)
class BrokerageInvestmentConfigAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'growth_rate',
        'initial_balance',
        'contribution_strategy',
        'contribution_percentage',
        'contribution_fixed_amount',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('contribution_strategy',)
    search_fields = ('name',)


@admin.register(BrokerageInvestmentTemplate)
class BrokerageInvestmentTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'growth_rate',
        'initial_balance',
        'contribution_strategy',
        'contribution_percentage',
        'contribution_fixed_amount',
        'template_description',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('contribution_strategy',)
    search_fields = ('name', 'template_description')


@admin.register(CashConfig)
class CashConfigAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'initial_amount',
        'cash_maintenance_strategy',
        'reserve_amount',
        'reserve_months',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('cash_maintenance_strategy',)
    search_fields = ('name',)


@admin.register(CashTemplate)
class CashTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'template_description',
        'cash_maintenance_strategy',
        'reserve_amount',
        'reserve_months',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('cash_maintenance_strategy',)
    search_fields = ('name', 'template_description')


@admin.register(DebtConfig)
class DebtConfigAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'principal',
        'interest_rate',
        'payment_minimum',
        'payment_strategy',
        'payment_fixed_amount',
        'payment_percentage',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('payment_strategy',)
    search_fields = ('name',)


@admin.register(DebtTemplate)
class DebtTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'template_description',
        'principal',
        'interest_rate',
        'payment_minimum',
        'payment_strategy',
        'payment_fixed_amount',
        'payment_percentage',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('payment_strategy',)
    search_fields = ('name', 'template_description')


@admin.register(ExpenseConfig)
class ExpenseConfigAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'amount',
        'type',
        'frequency',
        'is_essential',
        'is_tax_deductible',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('type', 'frequency', 'is_essential', 'is_tax_deductible')
    search_fields = ('name',)


@admin.register(ExpenseTemplate)
class ExpenseTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'template_description',
        'amount',
        'type',
        'frequency',
        'is_essential',
        'is_tax_deductible',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('type', 'frequency', 'is_essential', 'is_tax_deductible')
    search_fields = ('name', 'template_description')


@admin.register(IncomeConfig)
class IncomeConfigAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'gross_income',
        'growth_rate',
        'income_type',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('income_type',)
    search_fields = ('name',)


@admin.register(IncomeTemplate)
class IncomeTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'template_description',
        'gross_income',
        'growth_rate',
        'income_type',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('income_type',)
    search_fields = ('name', 'template_description')


@admin.register(IraInvestmentConfig)
class IraInvestmentConfigAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'ira_type',
        'growth_rate',
        'initial_balance',
        'contribution_strategy',
        'contribution_percentage',
        'contribution_fixed_amount',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('ira_type', 'contribution_strategy')
    search_fields = ('name',)


@admin.register(IraInvestmentTemplate)
class IraInvestmentTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'template_description',
        'ira_type',
        'growth_rate',
        'initial_balance',
        'contribution_strategy',
        'contribution_percentage',
        'contribution_fixed_amount',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('ira_type', 'contribution_strategy')
    search_fields = ('name', 'template_description')


@admin.register(RetirementConfig)
class RetirementConfigAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'life_expectancy',
        'retirement_strategy',
        'retirement_withdrawal_rate',
        'retirement_income_goal',
        'retirement_age',
        'retirement_savings_amount',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('retirement_strategy',)
    search_fields = ('name',)


@admin.register(RetirementTemplate)
class RetirementTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'template_description',
        'life_expectancy',
        'retirement_strategy',
        'retirement_withdrawal_rate',
        'retirement_income_goal',
        'retirement_age',
        'retirement_savings_amount',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('retirement_strategy',)
    search_fields = ('name', 'template_description')


@admin.register(TaxConfig)
class TaxConfigAdmin(admin.ModelAdmin):
    list_display = (
        'tax_strategy',
        'tax_rate',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('tax_strategy',)
    search_fields = ('tax_strategy',)


@admin.register(TaxTemplate)
class TaxTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'tax_strategy',
        'tax_rate',
        'template_description',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('tax_strategy',)
    search_fields = ('tax_strategy', 'template_description')


@admin.register(TaxDeferredInvestmentConfig)
class TaxDeferredInvestmentConfigAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'growth_rate',
        'initial_balance',
        'elective_contribution_strategy',
        'elective_contribution_percentage',
        'elective_contribution_fixed_amount',
        'employer_contributes',
        'employer_contribution_strategy',
        'employer_compensation_match_percentage',
        'employer_contribution_fixed_amount',
        'employer_match_percentage',
        'employer_match_percentage_limit',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('elective_contribution_strategy', 'employer_contributes', 'employer_contribution_strategy')
    search_fields = ('name',)


@admin.register(TaxDeferredInvestmentTemplate)
class TaxDeferredInvestmentTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'template_description',
        'growth_rate',
        'initial_balance',
        'elective_contribution_strategy',
        'elective_contribution_percentage',
        'elective_contribution_fixed_amount',
        'employer_contributes',
        'employer_contribution_strategy',
        'employer_compensation_match_percentage',
        'employer_contribution_fixed_amount',
        'employer_match_percentage',
        'employer_match_percentage_limit',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('elective_contribution_strategy', 'employer_contributes', 'employer_contribution_strategy')
    search_fields = ('name', 'template_description')


@admin.register(PlanConfig)
class PlanConfigAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'age',
        'year',
        'inflation_rate',
        'allow_negative_disposable_income',
        'retirement',
        'cash',
        'tax',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('allow_negative_disposable_income',)
    search_fields = ('name',)

    filter_horizontal = (
        'incomes',
        'expenses',
        'debts',
        'tax_deferred_investments',
        'brokerage_investments',
        'ira_investments',
    )


@admin.register(PlanTemplate)
class PlanTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'age',
        'year',
        'inflation_rate',
        'allow_negative_disposable_income',
        'retirement_template',
        'cash_template',
        'tax_template',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('allow_negative_disposable_income',)
    search_fields = ('name',)

    filter_horizontal = (
        'income_templates',
        'expense_templates',
        'debt_templates',
        'tax_deferred_investment_templates',
        'brokerage_investment_templates',
        'ira_investment_templates',
    )
