from django.test import TestCase
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from rest_framework.test import APIClient

from main.models import Plan, Income


class ManageRelatedModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
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

        cls.income1 = Income.objects.create(name="Income 1", gross_income=50000, growth_rate=5)
        cls.income2 = Income.objects.create(name="Income 2", gross_income=60000, growth_rate=3)

        cls.client = APIClient()

    def test_add_valid_related_model(self):
        url = f'/api/plans/{self.plan.id}/manage_related_model/'
        data = {
            "related_model": "incomes",
            "related_id": self.income1.id,
            "action": "add"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.plan.refresh_from_db()
        self.assertIn(self.income1, self.plan.incomes.all())

    def test_remove_valid_related_model(self):
        self.plan.incomes.add(self.income1)
        url = f'/api/plans/{self.plan.id}/manage_related_model/'
        data = {
            "related_model": "incomes",
            "related_id": self.income1.id,
            "action": "remove"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.plan.refresh_from_db()
        self.assertNotIn(self.income1, self.plan.incomes.all())

    def test_add_invalid_related_model(self):
        url = f'/api/plans/{self.plan.id}/manage_related_model/'
        data = {
            "related_model": "invalid_model",
            "related_id": self.income1.id,
            "action": "add"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_remove_invalid_related_model(self):
        url = f'/api/plans/{self.plan.id}/manage_related_model/'
        data = {
            "related_model": "invalid_model",
            "related_id": self.income1.id,
            "action": "remove"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_add_nonexistent_related_model_instance(self):
        nonexistent_id = 9999
        url = f'/api/plans/{self.plan.id}/manage_related_model/'
        data = {
            "related_model": "incomes",
            "related_id": nonexistent_id,
            "action": "add"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_remove_nonexistent_related_model_instance(self):
        nonexistent_id = 9999
        url = f'/api/plans/{self.plan.id}/manage_related_model/'
        data = {
            "related_model": "incomes",
            "related_id": nonexistent_id,
            "action": "remove"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_invalid_action(self):
        url = f'/api/plans/{self.plan.id}/manage_related_model/'
        data = {
            "related_model": "incomes",
            "related_id": self.income1.id,
            "action": "invalid_action"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertIn("action", response.data)

    def test_missing_action_field(self):
        url = f'/api/plans/{self.plan.id}/manage_related_model/'
        data = {
            "related_model": "incomes",
            "related_id": self.income1.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertIn("action", response.data)

    def test_missing_related_model_field(self):
        url = f'/api/plans/{self.plan.id}/manage_related_model/'
        data = {
            "related_id": self.income1.id,
            "action": "add"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertIn("related_model", response.data)

    def test_missing_related_id_field(self):
        url = f'/api/plans/{self.plan.id}/manage_related_model/'
        data = {
            "related_model": "incomes",
            "action": "add"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertIn("related_id", response.data)
