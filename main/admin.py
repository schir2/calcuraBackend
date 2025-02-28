from django import forms
from django.contrib import admin

from .models import Brokerage, BrokerageTemplate, CashReserve, CashReserveTemplate, Debt, \
    DebtTemplate, ExpenseTemplate, Income, IncomeTemplate, IraTemplate, \
    Ira, Expense, TaxDeferredTemplate, TaxDeferred, Plan, \
    PlanTemplate, RothIra, RothIraTemplate, Command, CommandSequence, CommandSequenceCommand


@admin.register(Brokerage)
class BrokerageConfigAdmin(admin.ModelAdmin):
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


@admin.register(BrokerageTemplate)
class BrokerageTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'growth_rate',
        'initial_balance',
        'contribution_strategy',
        'contribution_percentage',
        'contribution_fixed_amount',
        'description',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('contribution_strategy',)
    search_fields = ('name', 'description')


@admin.register(CashReserve)
class CashConfigAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'initial_amount',
        'cash_reserve_strategy',
        'reserve_amount',
        'reserve_months',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('cash_reserve_strategy',)
    search_fields = ('name',)


@admin.register(CashReserveTemplate)
class CashTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'cash_reserve_strategy',
        'reserve_amount',
        'reserve_months',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('cash_reserve_strategy',)
    search_fields = ('name', 'description')


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
        'description',
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
    search_fields = ('name', 'description')


@admin.register(Expense)
class ExpenseConfigAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'amount',
        'expense_type',
        'frequency',
        'is_essential',
        'is_tax_deductible',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('expense_type', 'frequency', 'is_essential', 'is_tax_deductible')
    search_fields = ('name',)


@admin.register(ExpenseTemplate)
class ExpenseTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'amount',
        'expense_type',
        'frequency',
        'is_essential',
        'is_tax_deductible',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('expense_type', 'frequency', 'is_essential', 'is_tax_deductible')
    search_fields = ('name', 'description')


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
        'description',
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
    search_fields = ('name', 'description')


@admin.register(Ira)
class IraConfigAdmin(admin.ModelAdmin):
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


@admin.register(IraTemplate)
class IraTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
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
    search_fields = ('name', 'description')


@admin.register(RothIra)
class RothIraConfigAdmin(admin.ModelAdmin):
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


@admin.register(RothIraTemplate)
class RothIraTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
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
    search_fields = ('name', 'description')


@admin.register(TaxDeferred)
class TaxDeferredConfigAdmin(admin.ModelAdmin):
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


@admin.register(TaxDeferredTemplate)
class TaxDeferredTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
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
    search_fields = ('name', 'description')


class PlanAdminForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.ModelMultipleChoiceField):
                field.required = False


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    form = PlanAdminForm
    list_display = (
        'name',
        'age',
        'year',
        'inflation_rate',
        'insufficient_funds_strategy',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('insufficient_funds_strategy',)
    search_fields = ('name',)

    autocomplete_fields = ('incomes', 'expenses', 'debts', 'tax_deferreds', 'brokerages', 'roth_iras', 'iras')


@admin.register(PlanTemplate)
class PlanTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'age',
        'year',
        'inflation_rate',
        'insufficient_funds_strategy',
        'created_at',
        'edited_at',
        'creator',
        'editor',
    )
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('insufficient_funds_strategy',)
    search_fields = ('name',)

    filter_horizontal = (
        'income_templates',
        'expense_templates',
        'debt_templates',
        'tax_deferred_investment_templates',
        'brokerage_investment_templates',
        'ira_investment_templates',
    )


@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "label", "manager_name", "manager_id", "action")
    search_fields = ("action",)
    list_filter = ("action",)


@admin.register(CommandSequence)
class CommandSequenceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "plan", "ordering_type")
    search_fields = ("name", "plan__name")
    list_filter = ("ordering_type",)


@admin.register(CommandSequenceCommand)
class CommandSequenceCommandAdmin(admin.ModelAdmin):
    list_display = ("id", "sequence", "command", "order", "is_active")
    search_fields = ("sequence__name",)
    list_filter = ("is_active",)
    ordering = ("sequence", "order")
