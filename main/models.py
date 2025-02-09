from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Max
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class BrokerageInvestmentABC(models.Model):
    class ContributionStrategy(models.TextChoices):
        FIXED = 'fixed', _('Fixed')
        PERCENTAGE_OF_INCOME = 'percentage_of_income', _('Percentage of Income')
        MAX = 'max', _('Max')

    name = models.CharField(max_length=255, verbose_name=_("Name"))
    growth_rate = models.FloatField(
        help_text=_("Annual growth rate as a percentage"),
        verbose_name=_("Growth Rate")
    )
    initial_balance = models.FloatField(
        help_text=_("Initial balance in the investment account"),
        verbose_name=_("Initial Balance")
    )

    contribution_strategy = models.CharField(
        max_length=50,
        choices=ContributionStrategy.choices,
        default=ContributionStrategy.FIXED,
        verbose_name=_("Contribution Strategy")
    )
    contribution_percentage = models.FloatField(
        null=True,
        blank=True,
        help_text=_("Percentage of income contributed annually"),
        verbose_name=_("Contribution Percentage")
    )
    contribution_fixed_amount = models.FloatField(
        null=True,
        blank=True,
        help_text=_("Fixed amount contributed annually"),
        verbose_name=_("Contribution Fixed Amount")
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class BrokerageInvestment(BaseModel, BrokerageInvestmentABC):
    class Meta:
        verbose_name = _("Brokerage Investment")
        verbose_name_plural = _("Brokerage Investment")


class BrokerageInvestmentTemplate(BaseModel, BrokerageInvestmentABC):
    """
    A template for creating BrokerageInvestmentConfig objects.
    """
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Template Description"),
        help_text=_("Description of the template for documentation purposes.")
    )

    class Meta:
        verbose_name = _("Brokerage Investment Template")
        verbose_name_plural = _("Brokerage Investment Templates")


class CashReserveABC(models.Model):
    class CashReserveStrategy(models.TextChoices):
        FIXED_CASH_RESERVE = 'fixed', _('Fixed Cash Reserve')
        VARIABLE_CASH_RESERVE = 'variable', _('Variable Cash Reserve')

    name = models.CharField(max_length=255, verbose_name=_("Name"))
    initial_amount = models.FloatField(
        verbose_name=_("Initial Amount"),
        help_text=_("The starting cash amount.")
    )
    cash_reserve_strategy = models.CharField(
        max_length=50,
        choices=CashReserveStrategy.choices,
        verbose_name=_("Cash Maintenance Strategy")
    )
    reserve_amount = models.FloatField(
        verbose_name=_("Reserve Amount"),
        help_text=_("The fixed cash reserve amount, if applicable."),
        null=True,
        blank=True
    )
    reserve_months = models.PositiveIntegerField(
        verbose_name=_("Reserve Months"),
        help_text=_("The number of months of cash to maintain in reserve."),
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class CashReserve(BaseModel, CashReserveABC):
    class Meta:
        verbose_name = _("Cash Reserve")
        verbose_name_plural = _("Cash Reserves")


class CashReserveTemplate(BaseModel, CashReserveABC):
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Template Description"),
        help_text=_("Description of the template for documentation purposes."),
    )

    class Meta:
        verbose_name = _("Cash Configuration Template")
        verbose_name_plural = _("Cash Configuration Templates")


class DebtABC(models.Model):
    class DebtPaymentStrategy(models.TextChoices):
        FIXED = 'fixed', _('Fixed Payment')
        MINIMUM_PAYMENT = 'minimum_payment', _('Minimum Payment')
        MAXIMUM_PAYMENT = 'maximum_payment', _('Maximum Payment')
        PERCENTAGE_OF_DEBT = 'percentage_of_debt', _('Percentage of Debt')

    name = models.CharField(max_length=255, verbose_name=_("Name"))
    principal = models.FloatField(
        verbose_name=_("Principal Amount"),
        help_text=_("The total debt amount.")
    )
    interest_rate = models.FloatField(
        verbose_name=_("Interest Rate"),
        help_text=_("Annual interest rate as a percentage.")
    )
    payment_minimum = models.FloatField(
        verbose_name=_("Minimum Payment"),
        help_text=_("The minimum required payment."),
        null=True,
        blank=True
    )
    payment_strategy = models.CharField(
        max_length=50,
        choices=DebtPaymentStrategy.choices,
        verbose_name=_("Payment Strategy")
    )
    payment_fixed_amount = models.FloatField(
        verbose_name=_("Fixed Payment Amount"),
        help_text=_("The fixed payment amount, if applicable."),
        null=True,
        blank=True
    )
    payment_percentage = models.FloatField(
        verbose_name=_("Payment Percentage"),
        help_text=_("Percentage of debt to pay each period, if applicable."),
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Debt(BaseModel, DebtABC):
    class Meta:
        verbose_name = _("Debt Configuration")
        verbose_name_plural = _("Debt Configurations")


class DebtTemplate(BaseModel, DebtABC):
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Template Description"),
        help_text=_("Description of the template for documentation purposes."),
    )

    class Meta:
        verbose_name = _("Debt Configuration Template")
        verbose_name_plural = _("Debt Configuration Templates")


class ExpenseABC(models.Model):
    class ExpenseType(models.TextChoices):
        FIXED = 'fixed', _('Fixed')
        VARIABLE = 'variable', _('Variable')

    class Frequency(models.TextChoices):
        MONTHLY = 'monthly', _('Monthly')
        WEEKLY = 'weekly', _('Weekly')
        BIWEEKLY = 'biweekly', _('Biweekly')
        QUARTERLY = 'quarterly', _('Quarterly')
        ANNUALLY = 'annual', _('Annually')
        ONE_TIME = 'one_time', _('One Time')

    name = models.CharField(max_length=255, verbose_name=_("Name"))
    amount = models.FloatField(
        verbose_name=_("Amount"),
        help_text=_("The expense amount.")
    )
    growth_rate = models.FloatField(
        verbose_name=_("Growth Rate"),
        help_text=_("The growth rate.")
    )
    expense_type = models.CharField(
        max_length=50,
        choices=ExpenseType.choices,
        verbose_name=_("Expense Type")
    )
    frequency = models.CharField(
        max_length=50,
        choices=Frequency.choices,
        verbose_name=_("Frequency")
    )
    is_essential = models.BooleanField(
        default=False,
        verbose_name=_("Is Essential"),
        help_text=_("Whether the expense is essential.")
    )
    grows_with_inflation = models.BooleanField(
        default=False,
        verbose_name=_("Grows with Inflation"),
        help_text=_("Whether the expense grows with inflation.")
    )
    is_tax_deductible = models.BooleanField(
        default=False,
        verbose_name=_("Is Tax Deductible"),
        help_text=_("Whether the expense is tax-deductible.")
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Expense(BaseModel, ExpenseABC):
    class Meta:
        verbose_name = _("Expense Configuration")
        verbose_name_plural = _("Expense Configurations")


class ExpenseTemplate(BaseModel, ExpenseABC):
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Template Description"),
        help_text=_("Description of the template for documentation purposes."),
    )

    class Meta:
        verbose_name = _("Expense Configuration Template")
        verbose_name_plural = _("Expense Configuration Templates")


class IncomeABC(models.Model):
    class IncomeType(models.TextChoices):
        ORDINARY = 'ordinary', _('Ordinary')

    class Frequency(models.TextChoices):
        WEEKLY = 'weekly', _('Weekly')
        MONTHLY = 'monthly', _('Monthly')
        QUARTERLY = 'quarterly', _('Quarterly')
        ANNUAL = 'annual', _('Annual')

    name = models.CharField(max_length=255, verbose_name=_("Name"))
    gross_income = models.FloatField(
        verbose_name=_("Gross Income"),
        help_text=_("The total annual gross income.")
    )
    growth_rate = models.FloatField(
        verbose_name=_("Growth Rate"),
        help_text=_("Annual growth rate as a percentage.")
    )
    income_type = models.CharField(
        max_length=50,
        choices=IncomeType.choices,
        default=IncomeType.ORDINARY,
        verbose_name=_("Income Type")
    )

    frequency = models.CharField(
        max_length=50,
        choices=Frequency.choices,
        default=Frequency.ANNUAL,
        verbose_name=_("Frequency")
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Income(BaseModel, IncomeABC):
    class Meta:
        verbose_name = _("Income Configuration")
        verbose_name_plural = _("Income Configurations")


class IncomeTemplate(BaseModel, IncomeABC):
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Template Description"),
        help_text=_("Description of the template for documentation purposes."),
    )

    class Meta:
        verbose_name = _("Income Configuration Template")
        verbose_name_plural = _("Income Configuration Templates")


class IraInvestmentABC(models.Model):
    class IraContributionStrategy(models.TextChoices):
        FIXED = 'fixed', _('Fixed')
        PERCENTAGE_OF_INCOME = 'percentage_of_income', _('Percentage of Income')
        MAX = 'max', _('Max')

    name = models.CharField(max_length=255, verbose_name=_("Name"))
    growth_rate = models.FloatField(
        verbose_name=_("Growth Rate"),
        help_text=_("Annual growth rate as a percentage.")
    )
    initial_balance = models.FloatField(
        verbose_name=_("Initial Balance"),
        help_text=_("Initial balance in the IRA account.")
    )
    contribution_strategy = models.CharField(
        max_length=50,
        choices=IraContributionStrategy.choices,
        default=IraContributionStrategy.FIXED,
        verbose_name=_("Contribution Strategy")
    )
    contribution_percentage = models.FloatField(
        null=True,
        blank=True,
        verbose_name=_("Contribution Percentage"),
        help_text=_("Percentage of income contributed annually.")
    )
    contribution_fixed_amount = models.FloatField(
        null=True,
        blank=True,
        verbose_name=_("Contribution Fixed Amount"),
        help_text=_("Fixed amount contributed annually.")
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class IraInvestment(BaseModel, IraInvestmentABC):
    income = models.ForeignKey(Income, on_delete=models.SET_NULL, null=True, verbose_name=_("Income"))

    class Meta:
        verbose_name = _("IRA Investment Configuration")
        verbose_name_plural = _("IRA Investment Configurations")


class IraInvestmentTemplate(BaseModel, IraInvestmentABC):
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Template Description"),
        help_text=_("Description of the template for documentation purposes."),
    )

    class Meta:
        verbose_name = _("IRA Investment Configuration Template")
        verbose_name_plural = _("IRA Investment Configuration Templates")


class RothIraInvestmentABC(models.Model):
    class RothIraContributionStrategy(models.TextChoices):
        FIXED = 'fixed', _('Fixed')
        PERCENTAGE_OF_INCOME = 'percentage_of_income', _('Percentage of Income')
        MAX = 'max', _('Max')

    name = models.CharField(max_length=255, verbose_name=_("Name"))
    growth_rate = models.FloatField(
        verbose_name=_("Growth Rate"),
        help_text=_("Annual growth rate as a percentage.")
    )
    initial_balance = models.FloatField(
        verbose_name=_("Initial Balance"),
        help_text=_("Initial balance in the IRA account.")
    )
    contribution_strategy = models.CharField(
        max_length=50,
        choices=RothIraContributionStrategy.choices,
        default=RothIraContributionStrategy.FIXED,
        verbose_name=_("Contribution Strategy")
    )
    contribution_percentage = models.FloatField(
        null=True,
        blank=True,
        verbose_name=_("Contribution Percentage"),
        help_text=_("Percentage of income contributed annually.")
    )
    contribution_fixed_amount = models.FloatField(
        null=True,
        blank=True,
        verbose_name=_("Contribution Fixed Amount"),
        help_text=_("Fixed amount contributed annually.")
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class RothIraInvestment(BaseModel, IraInvestmentABC):
    income = models.ForeignKey(Income, on_delete=models.SET_NULL, null=True, verbose_name=_("Income"))

    class Meta:
        verbose_name = _("Roth IRA Investment Configuration")
        verbose_name_plural = _("Roth IRA Investment Configurations")


class RothIraInvestmentTemplate(BaseModel, IraInvestmentABC):
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Template Description"),
        help_text=_("Description of the template for documentation purposes."),
    )

    class Meta:
        verbose_name = _("Roth IRA Investment Configuration Template")
        verbose_name_plural = _("Roth IRA Investment Configuration Templates")


class TaxDeferredInvestmentABC(models.Model):
    class EmployerContributionStrategy(models.TextChoices):
        NONE = 'none', _('None')
        PERCENTAGE_OF_CONTRIBUTION = 'percentage_of_contribution', _('Percentage of Contribution')
        PERCENTAGE_OF_COMPENSATION = 'percentage_of_compensation', _('Percentage of Compensation')
        FIXED = 'fixed', _('Fixed')

    class TaxDeferredContributionStrategy(models.TextChoices):
        NONE = 'none', _('None')
        UNTIL_COMPANY_MATCH = 'until_company_match', _('Until Company Match')
        PERCENTAGE_OF_INCOME = 'percentage_of_income', _('Percentage of Income')
        FIXED = 'fixed', _('Fixed')
        MAX = 'max', _('Max')

    name = models.CharField(max_length=255, verbose_name=_("Name"))
    growth_rate = models.FloatField(
        verbose_name=_("Growth Rate"),
        help_text=_("Annual growth rate as a percentage.")
    )
    initial_balance = models.FloatField(
        verbose_name=_("Initial Balance"),
        help_text=_("Initial balance in the tax-deferred investment account.")
    )

    elective_contribution_strategy = models.CharField(
        max_length=50,
        choices=TaxDeferredContributionStrategy.choices,
        verbose_name=_("Elective Contribution Strategy")
    )
    elective_contribution_percentage = models.FloatField(
        null=True,
        blank=True,
        verbose_name=_("Elective Contribution Percentage"),
        help_text=_("Percentage of income contributed annually.")
    )
    elective_contribution_fixed_amount = models.FloatField(
        null=True,
        blank=True,
        verbose_name=_("Elective Contribution Fixed Amount"),
        help_text=_("Fixed amount contributed annually.")
    )

    employer_contributes = models.BooleanField(
        default=False,
        verbose_name=_("Employer Contributes"),
        help_text=_("Whether the employer contributes to the account.")
    )
    employer_contribution_strategy = models.CharField(
        max_length=50,
        choices=EmployerContributionStrategy.choices,
        verbose_name=_("Employer Contribution Strategy"),
        null=True,
        blank=True
    )
    employer_compensation_match_percentage = models.FloatField(
        null=True,
        blank=True,
        verbose_name=_("Employer Compensation Match Percentage"),
        help_text=_("Percentage of compensation matched by the employer.")
    )
    employer_contribution_fixed_amount = models.FloatField(
        null=True,
        blank=True,
        verbose_name=_("Employer Contribution Fixed Amount"),
        help_text=_("Fixed amount contributed by the employer annually.")
    )
    employer_match_percentage = models.FloatField(
        null=True,
        blank=True,
        verbose_name=_("Employer Match Percentage"),
        help_text=_("Percentage of employee contributions matched by the employer.")
    )
    employer_match_percentage_limit = models.FloatField(
        null=True,
        blank=True,
        verbose_name=_("Employer Match Percentage Limit"),
        help_text=_("Limit on the percentage of employee contributions matched by the employer.")
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True





class TaxDeferredInvestment(BaseModel, TaxDeferredInvestmentABC):
    income = models.ForeignKey(Income, on_delete=models.SET_NULL, null=True, verbose_name=_("Income"))

    class Meta:
        verbose_name = _("Tax-Deferred Investment Configuration")
        verbose_name_plural = _("Tax-Deferred Investment Configurations")


class TaxDeferredInvestmentTemplate(BaseModel, TaxDeferredInvestmentABC):
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Template Description"),
        help_text=_("Description of the template for documentation purposes."),
    )

    class Meta:
        verbose_name = _("Tax-Deferred Investment Configuration Template")
        verbose_name_plural = _("Tax-Deferred Investment Configuration Templates")


class PlanABC(models.Model):
    class InsufficientFundsStrategy(models.TextChoices):
        NONE = 'none', _('None')
        MINIMUM_ONLY = 'minimum_only', _('Minimum Only')
        FULL = 'full', _('Full')

    class GrowthApplicationStrategy(models.TextChoices):
        START = 'start', _('Start')
        END = 'end', _('End')

    class RetirementStrategy(models.TextChoices):
        DEBT_FREE = 'debt_free', _('Debt-Free')
        AGE = 'age', _('Age-Based')
        PERCENT_RULE = 'percent_rule', _('Percentage Rule')
        TARGET_SAVINGS = 'target_savings', _('Target Savings')

    class IncomeTaxStrategy(models.TextChoices):
        SIMPLE = 'simple', _('Simple')

    name = models.CharField(max_length=255, verbose_name=_("Name"))
    age = models.PositiveIntegerField(verbose_name=_("Age"), default=settings.DEFAULT_AGE, blank=True, null=True)
    year = models.PositiveIntegerField(verbose_name=_("Year"), default=timezone.now().year, blank=True, null=True)
    inflation_rate = models.FloatField(
        verbose_name=_("Inflation Rate"),
        help_text=_("Annual inflation rate as a percentage.")
    )
    insufficient_funds_strategy = models.CharField(
        max_length=50,
        choices=InsufficientFundsStrategy.choices,
        verbose_name=_("Insufficient Funds Strategy"),
        default=InsufficientFundsStrategy.NONE
    )

    growth_rate = models.FloatField(
        verbose_name=_("Growth Rate"),
        help_text=_("Annual Growth rate as a percentage.")
    )

    growth_application_strategy = models.CharField(
        max_length=50,
        choices=GrowthApplicationStrategy.choices,
        verbose_name=_("Growth Application Strategy"),
        default=GrowthApplicationStrategy.START
    )

    cash_reserves = models.ManyToManyField(
        'CashReserve',
        related_name='plans',
        verbose_name=_("Cash Configuration"),
    )

    # Many-to-Many Relationships
    incomes = models.ManyToManyField(
        'Income',
        related_name='plans',
        verbose_name=_("Income Configurations"),
    )
    expenses = models.ManyToManyField(
        'Expense',
        related_name='plans',
        verbose_name=_("Expense Configurations")
    )
    debts = models.ManyToManyField(
        'Debt',
        related_name='plans',
        verbose_name=_("Debt Configurations")
    )
    tax_deferred_investments = models.ManyToManyField(
        'TaxDeferredInvestment',
        related_name='plans',
        verbose_name=_("Tax-Deferred Investment Configurations")
    )
    brokerage_investments = models.ManyToManyField(
        'BrokerageInvestment',
        related_name='plans',
        verbose_name=_("Brokerage Investment Configurations")
    )
    ira_investments = models.ManyToManyField(
        'IraInvestment',
        related_name='plans',
        verbose_name=_("IRA Investment Configurations")
    )
    roth_ira_investments = models.ManyToManyField(
        'RothIraInvestment',
        related_name='plans',
        verbose_name=_("Roth IRA Investment Configurations")
    )

    life_expectancy = models.PositiveIntegerField(
        verbose_name=_("Life Expectancy"),
        help_text=_("Estimated life expectancy in years.")
    )
    retirement_strategy = models.CharField(
        max_length=50,
        choices=RetirementStrategy.choices,
        verbose_name=_("Retirement Strategy")
    )
    retirement_withdrawal_rate = models.FloatField(
        verbose_name=_("Retirement Withdrawal Rate"),
        help_text=_("Annual withdrawal rate as a percentage."),
        null=True
    )
    retirement_income_goal = models.FloatField(
        verbose_name=_("Retirement Income Goal"),
        help_text=_("Annual income goal during retirement."),
        null=True,
    )
    retirement_age = models.PositiveIntegerField(
        verbose_name=_("Retirement Age"),
        help_text=_("The age at which retirement starts."),
        default=settings.DEFAULT_RETIREMENT_AGE
    )
    retirement_savings_amount = models.FloatField(
        verbose_name=_("Retirement Savings Amount"),
        help_text=_("Initial savings amount at the time of retirement."),
        null=True,
    )

    retirement_income_adjusted_for_inflation = models.BooleanField(
        verbose_name=_("Retirement Income Adjusted For Inflation"),
        help_text=_("Inflation adjusted for inflation."),
        default=True
    )

    tax_strategy = models.CharField(
        max_length=50,
        choices=IncomeTaxStrategy.choices,
        default=IncomeTaxStrategy.SIMPLE,
        verbose_name=_("Tax Strategy")
    )
    tax_rate = models.FloatField(
        verbose_name=_("Tax Rate"),
        help_text=_("Applicable tax rate as a percentage.")
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Plan(BaseModel, PlanABC):
    class Meta:
        verbose_name = _("Plan Configuration")
        verbose_name_plural = _("Plan Configurations")


class PlanTemplate(BaseModel):
    class InsufficientFundsStrategy(models.TextChoices):
        NONE = 'none', _('None')
        MINIMUM_ONLY = 'minimum_only', _('Minimum Only')
        FULL = 'full', _('Full')

    name = models.CharField(max_length=255, verbose_name=_("Name"))
    age = models.PositiveIntegerField(verbose_name=_("Age"), blank=True, null=True)
    year = models.PositiveIntegerField(verbose_name=_("Year"), blank=True, null=True)
    inflation_rate = models.FloatField(
        verbose_name=_("Inflation Rate"),
        help_text=_("Annual inflation rate as a percentage."),
        blank=True, null=True
    )
    insufficient_funds_strategy = models.CharField(
        max_length=50,
        choices=InsufficientFundsStrategy.choices,
        verbose_name=_("Insufficient Funds Strategy"),
        default=InsufficientFundsStrategy.NONE
    )

    cash_reserve_templates = models.ForeignKey(
        'CashReserveTemplate',
        on_delete=models.CASCADE,
        related_name='plan_templates',
        verbose_name=_("Cash Template"),
        blank=True,
        null=True,
    )
    income_templates = models.ManyToManyField(
        'IncomeTemplate',
        related_name='plan_templates',
        verbose_name=_("Income Templates"),
        blank=True,
    )
    expense_templates = models.ManyToManyField(
        'ExpenseTemplate',
        related_name='plan_templates',
        verbose_name=_("Expense Templates"),
        blank=True,
    )
    debt_templates = models.ManyToManyField(
        'DebtTemplate',
        related_name='plan_templates',
        verbose_name=_("Debt Templates"),
        blank=True,
    )
    tax_deferred_investment_templates = models.ManyToManyField(
        'TaxDeferredInvestmentTemplate',
        related_name='plan_templates',
        verbose_name=_("Tax-Deferred Investment Templates"),
        blank=True,
    )
    brokerage_investment_templates = models.ManyToManyField(
        'BrokerageInvestmentTemplate',
        related_name='plan_templates',
        verbose_name=_("Brokerage Investment Templates"),
        blank=True,
    )
    ira_investment_templates = models.ManyToManyField(
        'IraInvestmentTemplate',
        related_name='plan_templates',
        verbose_name=_("IRA Investment Templates"),
        blank=True,
    )
    roth_ira_investment_templates = models.ManyToManyField(
        'RothIraInvestmentTemplate',
        related_name='plan_templates',
        verbose_name=_("Roth IRA Investment Templates"),
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Plan Template")
        verbose_name_plural = _("Plan Templates")


class Command(models.Model):
    """ A command that applies an action to any model (Expense, Income, Debt, etc.) """

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    related_object = GenericForeignKey("content_type", "object_id")
    action = models.CharField(max_length=255, verbose_name=_("Action"))

    @property
    def name(self):
        return str(self.related_object)

    @property
    def label(self):
        return getattr(self.related_object, "label", str(self.related_object))

    @property
    def manager_name(self):
        name = self.content_type.model_class().__name__
        return f'{name[0].lower()}{name[1:]}Managers'

    @property
    def manager_id(self):
        return self.object_id

    def __str__(self):
        return f"{self.label} ({self.action})"


class CommandSequence(BaseModel):
    class OrderingType(models.TextChoices):
        PREDEFINED = "predefined", _("Predefined")
        CUSTOM = "custom", _("Custom")

    name = models.CharField(max_length=255, verbose_name=_("Name"))
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name="command_sequences", verbose_name=_("Plan"))
    ordering_type = models.CharField(
        max_length=50,
        choices=OrderingType.choices,
        default=OrderingType.CUSTOM,
        verbose_name=_("Ordering Type")
    )

    def get_commands(self):
        return self.sequence_commands.all().order_by('order')

    def order_commands(self):
        pass

    def get_max_order(self):
        max_order = self.sequence_commands.aggregate(max_order=Max('order'))['max_order']
        return max_order or 0

    def __str__(self):
        return f'{self.name} {self.ordering_type}'


class CommandSequenceCommand(models.Model):
    sequence = models.ForeignKey(CommandSequence, on_delete=models.CASCADE, related_name="sequence_commands")
    command = models.ForeignKey(Command, on_delete=models.CASCADE, related_name="command_instances")
    order = models.PositiveIntegerField(verbose_name=_("Order"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))

    class Meta:
        unique_together = ("sequence", "command")
        ordering = ["order"]

    def __str__(self):
        return f'{self.sequence.plan} {self.sequence} ({self.command})'