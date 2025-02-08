from django.test import TestCase
from django.contrib.contenttypes.models import ContentType
from main.models import Plan, Command, CommandSequence, CommandSequenceCommand, Debt

class CommandSequenceTests(TestCase):
    def setUp(self):
        """Setup a Plan and related models for testing."""
        self.plan = Plan.objects.create(name="Retirement Plan")
        self.debt1 = Debt.objects.create(name="Car Loan", principal=15000, interest_rate=4.5)
        self.debt2 = Debt.objects.create(name="Mortgage", principal=250000, interest_rate=3.2)

    def test_command_sequence_created_when_debt_added(self):
        """Ensure a CommandSequence is created when a Debt is added to a Plan."""
        self.assertEqual(CommandSequence.objects.filter(plan=self.plan).count(), 0)

        # Add debt to plan
        self.plan.debts.add(self.debt1)

        # Now, a sequence should exist
        self.assertEqual(CommandSequence.objects.filter(plan=self.plan).count(), 1)

    def test_command_created_and_linked(self):
        """Ensure a predefined command is linked when a Debt is added to a Plan."""
        self.plan.debts.add(self.debt1)

        # Check if the Command exists
        content_type = ContentType.objects.get_for_model(Debt)
        command = Command.objects.filter(content_type=content_type, object_id=self.debt1.id).first()
        self.assertIsNotNone(command)

        # Ensure the command is linked to the sequence
        sequence = CommandSequence.objects.get(plan=self.plan)
        self.assertTrue(CommandSequenceCommand.objects.filter(sequence=sequence, command=command).exists())

    def test_commands_are_ordered_correctly(self):
        """Ensure that commands are added with the correct order values."""
        self.plan.debts.add(self.debt1)
        self.plan.debts.add(self.debt2)

        sequence = CommandSequence.objects.get(plan=self.plan)
        commands = list(CommandSequenceCommand.objects.filter(sequence=sequence).order_by("order"))

        # Ensure they are ordered correctly
        self.assertEqual(commands[0].command.object_id, self.debt1.id)
        self.assertEqual(commands[1].command.object_id, self.debt2.id)
        self.assertEqual(commands[0].order, 0)
        self.assertEqual(commands[1].order, 1)
