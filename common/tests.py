from django.test import TestCase

from common.utils.db_utils import get_many_to_many_fields  # Assuming the function is in utils.py
from main.models import Plan, Income, Expense


class GetManyToManyFieldsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create some related models for testing
        cls.income1 = Income.objects.create(name="Income 1", gross_income=50000, growth_rate=5)
        cls.income2 = Income.objects.create(name="Income 2", gross_income=60000, growth_rate=3)

        cls.expense1 = Expense.objects.create(name="Expense 1", amount=1000, type="fixed", frequency="monthly")
        cls.expense2 = Expense.objects.create(name="Expense 2", amount=2000, type="variable", frequency="yearly")

        cls.plan = Plan.objects.create(
            name="Test Plan",
            age=30,
            year=2024,
            inflation_rate=2.5,
            life_expectancy=85,
            retirement_strategy="age",
            retirement_withdrawal_rate=4,
            retirement_income_goal=40000,
            retirement_age=65,
            retirement_savings_amount=100000,
            tax_strategy="simple",
            tax_rate=15
        )

        # Add many-to-many relationships
        cls.plan.incomes.add(cls.income1, cls.income2)
        cls.plan.expenses.add(cls.expense1, cls.expense2)

    def test_many_to_many_field_names(self):
        # Check if get_many_to_many_fields returns correct field names
        expected_fields = ["cashes", "incomes", "expenses", "debts", "tax_deferred_investments",
                           "brokerage_investments", "ira_investments"]
        actual_fields = get_many_to_many_fields(Plan)
        self.assertListEqual(sorted(actual_fields), sorted(expected_fields))

    def test_no_many_to_many_fields_in_non_related_model(self):
        # Create a model without many-to-many fields
        class MockModel:
            class _meta:
                @staticmethod
                def get_fields():
                    return []

        self.assertEqual(get_many_to_many_fields(MockModel), [])

    def test_many_to_many_field_values(self):
        # Ensure that the related data is properly linked in a Plan instance
        plan = Plan.objects.first()

        self.assertEqual(set(plan.incomes.all()), {self.income1, self.income2})
        self.assertEqual(set(plan.expenses.all()), {self.expense1, self.expense2})
