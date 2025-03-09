from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.serializers import UserSerializer

User = get_user_model()

from main.models import (
    Brokerage,
    BrokerageTemplate,
    CashReserve,
    CashReserveTemplate,
    Debt,
    DebtTemplate,
    Expense,
    ExpenseTemplate,
    Income,
    IncomeTemplate,
    Ira,
    IraTemplate,
    TaxDeferred,
    TaxDeferredTemplate, Plan,
    PlanTemplate, RothIra, RothIraTemplate, CommandSequence, CommandSequenceCommand, Command, Hsa,
)

MANY_TO_MANY_FIELDS = [
    ('cash_reserves', CashReserve),
    ('incomes', Income),
    ('expenses', Expense),
    ('debts', Debt),
    ('tax_deferreds', TaxDeferred),
    ('brokerages', Brokerage),
    ('iras', Ira),
    ('roth_iras', RothIra),
    ('hsas', Hsa)
]


class BrokerageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brokerage
        fields = '__all__'


class BrokerageTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrokerageTemplate
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


class HsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hsa
        fields = '__all__'


class IncomeTemplateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = IncomeTemplate
        fields = '__all__'


class IraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ira
        fields = '__all__'


class IraTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IraTemplate
        fields = '__all__'


class RothIraSerializer(serializers.ModelSerializer):
    class Meta:
        model = RothIra
        fields = '__all__'


class RothIraTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RothIraTemplate
        fields = '__all__'


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


class TaxDeferredSerializer(serializers.ModelSerializer):
    income = IncomeOrIdField(required=False, many=False, allow_null=True)

    class Meta:
        model = TaxDeferred
        fields = '__all__'


SERIALIZER_MAP = {
    'CashReserve': CashReserveSerializer,
    'Debt': DebtSerializer,
    'Expense': ExpenseSerializer,
    'Income': IncomeSerializer,
    'Brokerage': BrokerageSerializer,
    'Ira': IraSerializer,
    'RothIra': RothIraSerializer,
    'TaxDeferred': TaxDeferredSerializer,
}


class TaxDeferredTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxDeferredTemplate
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
            model_name = f'{command.model_name[0].lower()}{command.model_name[1:]}'
            model_id = command.object_id

            commands.append({
                "command_id": command.id,
                "command_sequence_command_id": csc.id,
                "order": csc.order,
                "name": command.name,
                "label": command.label,
                "model_name": model_name,
                "model_id": model_id,
                "action": command.action,
                "is_active": csc.is_active,
            })
        return commands

    def to_internal_value(self, data):
        commands = data.pop("commands") if 'commands' in data else []
        data = super().to_internal_value(data)
        if commands:
            data['commands'] = commands
        return data

    def update(self, instance, validated_data):
        commands = validated_data.pop("commands") if 'commands' in validated_data else []
        instance = super().update(instance, validated_data)

        command_data_map = {cmd["command_sequence_command_id"]: cmd for cmd in commands}
        command_sequence_commands = CommandSequenceCommand.objects.filter(pk__in=command_data_map.keys())

        for csc in command_sequence_commands:
            command_data = command_data_map.get(csc.pk)
            if command_data:
                csc.order = command_data["order"]
                csc.is_active = command_data["is_active"]

        CommandSequenceCommand.objects.bulk_update(command_sequence_commands, ["order", "is_active"])

        return instance

    class Meta:
        model = CommandSequence
        fields = ('id', 'name', 'ordering_type', 'commands', 'plan')


class PlanSerializer(serializers.ModelSerializer):
    creator_details = UserSerializer(read_only=True, source='creator')
    editor_details = UserSerializer(read_only=True, source='editor')
    cash_reserves = CashReserveSerializer(required=False, many=True, read_only=True)
    incomes = IncomeSerializer(required=False, many=True, read_only=True)
    expenses = ExpenseSerializer(required=False, many=True, read_only=True)
    debts = DebtSerializer(required=False, many=True, read_only=True)
    tax_deferreds = TaxDeferredSerializer(required=False, many=True, read_only=True)
    brokerages = BrokerageSerializer(required=False, many=True, read_only=True)
    iras = IraSerializer(required=False, many=True, read_only=True)
    roth_iras = RothIraSerializer(required=False, many=True, read_only=True)
    command_sequences = CommandSequenceSerializer(required=False, many=True, read_only=True)

    class Meta:
        model = Plan
        fields = '__all__'


class PlanTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanTemplate
        fields = '__all__'


class ManageRelatedModelSerializer(serializers.Serializer):
    related_model = serializers.CharField(max_length=255)
    related_id = serializers.IntegerField()
    action = serializers.ChoiceField(choices=['add', 'remove'])
