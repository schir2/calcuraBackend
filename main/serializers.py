from django.contrib.auth import get_user_model
from django.db.models import QuerySet
from rest_framework import serializers

from users.serializers import UserSerializer

User = get_user_model()


class IncomeOrIdField(serializers.BaseSerializer):
    def to_internal_value(self, data):
        if isinstance(data, Income):
            return data
        income_id = None
        if isinstance(data, int):
            income_id = data
        elif isinstance(data, dict):
            income_id = data.get("id", None)

        if isinstance(income_id, int):
            try:
                return Income.objects.get(id=income_id)
            except Income.DoesNotExist:
                raise serializers.ValidationError(
                    f"Income with ID {income_id} does not exist."
                )

        elif isinstance(data, dict):
            # If a dict includes an `id`, assume partial update of an existing object
            income_id = data.get("id", None)
            if income_id:
                try:
                    instance = Income.objects.get(id=income_id)
                    serializer = IncomeSerializer(instance, data=data, partial=True)
                except Income.DoesNotExist:
                    raise serializers.ValidationError(
                        f"Income with ID {income_id} does not exist."
                    )
            else:
                # Create new Income if no ID is given
                serializer = IncomeSerializer(data=data)

            serializer.is_valid(raise_exception=True)
            return serializer.save()

        else:
            raise serializers.ValidationError(
                "Invalid input format. Must be either an ID or an object."
            )

    def to_representation(self, value):
        return IncomeSerializer(value).data


from .models import (
    BrokerageInvestment,
    BrokerageInvestmentTemplate,
    CashReserve,
    CashReserveTemplate,
    Debt,
    DebtTemplate,
    Expense,
    ExpenseTemplate,
    Income,
    IncomeTemplate,
    IraInvestment,
    IraInvestmentTemplate,
    TaxDeferredInvestment,
    TaxDeferredInvestmentTemplate,
    Plan,
    PlanTemplate, RothIraInvestment, RothIraInvestmentTemplate, CommandSequence, CommandSequenceCommand, Command,
)

MANY_TO_MANY_FIELDS = [
    ('cash_reserves', CashReserve),
    ('incomes', Income),
    ('expenses', Expense),
    ('debts', Debt),
    ('tax_deferred_investments', TaxDeferredInvestment),
    ('brokerage_investments', BrokerageInvestment),
    ('ira_investments', IraInvestment),
    ('roth_ira_investments', RothIraInvestment),
]


class BrokerageInvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrokerageInvestment
        fields = '__all__'


class BrokerageInvestmentTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrokerageInvestmentTemplate
        fields = '__all__'


class CashReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashReserve
        fields = '__all__'


class CashTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashReserveTemplate
        fields = '__all__'


class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = '__all__'


class DebtTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebtTemplate
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class ExpenseTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseTemplate
        fields = '__all__'


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'


class IncomeTemplateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = IncomeTemplate
        fields = '__all__'


class IraInvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IraInvestment
        fields = '__all__'


class IraInvestmentTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IraInvestmentTemplate
        fields = '__all__'


class RothIraInvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RothIraInvestment
        fields = '__all__'


class RothIraInvestmentTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RothIraInvestmentTemplate
        fields = '__all__'


class TaxDeferredInvestmentSerializer(serializers.ModelSerializer):
    income = IncomeOrIdField(required=False, many=False, allow_null=True)

    class Meta:
        model = TaxDeferredInvestment
        fields = '__all__'


SERIALIZER_MAP = {
    'CashReserve': CashReserveSerializer,
    'Debt': DebtSerializer,
    'Expense': ExpenseSerializer,
    'Income': IncomeSerializer,
    'BrokerageInvestment': BrokerageInvestmentSerializer,
    'IraInvestment': IraInvestmentSerializer,
    'RothIraInvestment': RothIraInvestmentSerializer,
    'TaxDeferredInvestment': TaxDeferredInvestmentSerializer,
}


class TaxDeferredInvestmentTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxDeferredInvestmentTemplate
        fields = '__all__'


class CommandSequenceCommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommandSequenceCommand
        fields = '__all__'


class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = '__all__'


class CommandSequenceSerializer(serializers.ModelSerializer):
    commands = serializers.SerializerMethodField()

    def get_commands(self, obj):
        commands = []
        for csc in obj.get_commands():
            command = csc.command
            manager_name = command.manager_name
            manager_id = command.object_id

            commands.append({
                "command_id": command.id,
                "command_sequence_command_id": csc.id,
                "order": csc.order,
                "name": command.name,
                "label": command.label,
                "manager_name": manager_name,
                "manager_id": manager_id,
                "action": command.action,
                "is_active": csc.is_active,
            })
        return commands

    def to_internal_value(self, data):
        commands = data.pop("commands")
        data = super().to_internal_value(data)
        data['commands'] = commands
        return data

    def update(self, instance, validated_data):
        commands = validated_data.pop("commands")
        instance = super().update(instance, validated_data)
        command_sequence_commands = CommandSequenceCommand.objects.filter(pk__in=[command['command_sequence_command_id'] for command in commands])
        for index, csc in enumerate(command_sequence_commands):
            csc.order = commands[index]['order']
            csc.is_active = commands[index]['is_active']
        return instance

    class Meta:
        model = CommandSequence
        fields = ('id', 'name', 'ordering_type', 'commands')


class PlanSerializer(serializers.ModelSerializer):
    creator_details = UserSerializer(read_only=True, source='creator')
    editor_details = UserSerializer(read_only=True, source='editor')
    cash_reserves = CashReserveSerializer(required=False, many=True, read_only=True)
    incomes = IncomeSerializer(required=False, many=True, read_only=True)
    expenses = ExpenseSerializer(required=False, many=True, read_only=True)
    debts = DebtSerializer(required=False, many=True, read_only=True)
    tax_deferred_investments = TaxDeferredInvestmentSerializer(required=False, many=True, read_only=True)
    brokerage_investments = BrokerageInvestmentSerializer(required=False, many=True, read_only=True)
    ira_investments = IraInvestmentSerializer(required=False, many=True, read_only=True)
    roth_ira_investments = RothIraInvestmentSerializer(required=False, many=True, read_only=True)
    commands = serializers.SerializerMethodField()
    command_sequences = CommandSequenceSerializer(required=False, many=True, read_only=True)

    class Meta:
        model = Plan
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        is_many = isinstance(instance, QuerySet)
        if not is_many:
            data['commands'] = self.get_commands(instance)

        return data

    def get_commands(self, plan: Plan):
        sequence = plan.command_sequences.first()
        if not sequence:
            return []

        commands = []
        for csc in sequence.get_commands():
            command = csc.command
            manager_name = command.manager_name
            manager_id = command.object_id

            commands.append({
                "commandId": command.id,
                "order": csc.order,
                "name": command.name,
                "label": command.label,
                "managerName": manager_name,
                "managerId": manager_id,
                "action": command.action,
            })

        return commands


class PlanTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanTemplate
        fields = '__all__'


class ManageRelatedModelSerializer(serializers.Serializer):
    related_model = serializers.CharField(max_length=255)
    related_id = serializers.IntegerField()
    action = serializers.ChoiceField(choices=['add', 'remove'])
