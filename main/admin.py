from django.contrib import admin

from .models import BrokerageInvestment, BrokerageInvestmentTemplate, Cash, CashTemplate, Debt, \
    DebtTemplate, ExpenseTemplate, Income, IncomeTemplate, IraInvestmentTemplate, \
    IraInvestment, Expense, TaxDeferredInvestmentTemplate, TaxDeferredInvestment, Plan, \
    PlanTemplate


@admin.register(BrokerageInvestment)
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


@admin.register(Cash)
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


@admin.register(Debt)
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


@admin.register(Expense)
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


@admin.register(Income)
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


@admin.register(IraInvestment)
class IraInvestmentConfigAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_contribution_tax_deferred',
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
    list_filter = ('is_contribution_tax_deferred', 'contribution_strategy')
    search_fields = ('name',)


@admin.register(IraInvestmentTemplate)
class IraInvestmentTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'template_description',
        'is_contribution_tax_deferred',
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
    list_filter = ('is_contribution_tax_deferred', 'contribution_strategy')
    search_fields = ('name', 'template_description')


@admin.register(TaxDeferredInvestment)
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


@admin.register(Plan)
class PlanConfigAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'age',
        'year',
        'inflation_rate',
        'allow_negative_disposable_income',
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
        'cash_template',
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
