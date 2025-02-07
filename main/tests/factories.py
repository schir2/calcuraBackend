import factory
from django.contrib.contenttypes.models import ContentType
from main.models import (
    Plan, Debt, Expense, Income, TaxDeferredInvestment,
    BrokerageInvestment, IraInvestment, RothIraInvestment, CashReserve,
    Command, CommandSequence, CommandSequenceCommand
)

class PlanFactory(factory.django.DjangoModelFactory):
    """ Factory for creating Plan objects """
    class Meta:
        model = Plan

    name = factory.Faker("word")
    age = factory.Faker("random_int", min=30, max=65)
    year = factory.Faker("random_int", min=2020, max=2030)
    inflation_rate = factory.Faker("pyfloat", positive=True, left_digits=2, right_digits=2)

class DebtFactory(factory.django.DjangoModelFactory):
    """ Factory for creating Debt objects """
    class Meta:
        model = Debt

    name = factory.Faker("word")
    principal = factory.Faker("pyfloat", positive=True, left_digits=5, right_digits=2)
    interest_rate = factory.Faker("pyfloat", positive=True, left_digits=2, right_digits=2)

class IncomeFactory(factory.django.DjangoModelFactory):
    """ Factory for creating Income objects """
    class Meta:
        model = Income

    name = factory.Faker("word")
    gross_income = factory.Faker("pyfloat", positive=True, left_digits=5, right_digits=2)
    growth_rate = factory.Faker("pyfloat", positive=True, left_digits=2, right_digits=2)

class CommandFactory(factory.django.DjangoModelFactory):
    """ Factory for creating Command objects """
    class Meta:
        model = Command

    content_type = factory.LazyAttribute(lambda _: ContentType.objects.get_for_model(Debt))
    object_id = factory.LazyAttribute(lambda _: DebtFactory().id)
    action = "process"

class CommandSequenceFactory(factory.django.DjangoModelFactory):
    """ Factory for creating CommandSequence objects """
    class Meta:
        model = CommandSequence

    name = factory.Faker("word")
    plan = factory.SubFactory(PlanFactory)
    ordering_type = "custom"

class CommandSequenceCommandFactory(factory.django.DjangoModelFactory):
    """ Factory for creating CommandSequenceCommand objects """
    class Meta:
        model = CommandSequenceCommand

    sequence = factory.SubFactory(CommandSequenceFactory)
    command = factory.SubFactory(CommandFactory)
    order = factory.Sequence(lambda n: n)
    is_active = True
