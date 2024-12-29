from rest_framework import serializers

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
    PlanTemplate, RothIraInvestment, RothIraInvestmentTemplate,
)


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
    class Meta:
        model = TaxDeferredInvestment
        fields = '__all__'


class TaxDeferredInvestmentTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxDeferredInvestmentTemplate
        fields = '__all__'


class PlanSerializer(serializers.ModelSerializer):
    cash_reserves = CashReserveSerializer(required=False, many=True)
    incomes = IncomeSerializer(required=False, many=True)
    expenses = ExpenseSerializer(required=False, many=True)
    debts = DebtSerializer(required=False, many=True)
    tax_deferred_investments = TaxDeferredInvestmentSerializer(required=False, many=True)
    brokerage_investments = BrokerageInvestmentSerializer(required=False, many=True)
    ira_investments = IraInvestmentSerializer(required=False, many=True)

    class Meta:
        model = Plan
        fields = '__all__'

    def process_related_field(self, field_name, related_model, related_data):
        validated_objects = []
        for item in related_data:
            if isinstance(item, int):
                try:
                    obj = related_model.objects.get(id=item)
                    validated_objects.append(obj)
                except related_model.DoesNotExist:
                    raise serializers.ValidationError({field_name: f'Object with ID {item} does not exist'})
            elif isinstance(item, dict):
                serializer_class = self.get_related_serializer_class(related_model)
                obj_serializer = serializer_class(data=item)
                obj_serializer.is_valid(raise_exception=True)
                validated_objects.append(obj_serializer.save())
            else:
                raise serializers.ValidationError({field_name: "Each item must be either an ID or an object."})
        return validated_objects

    def get_related_serializer_class(self, related_model):
        related_serializers = {
            'CashConfig': CashReserveSerializer,
            'IncomeConfig': IncomeSerializer,
            'ExpenseConfig': ExpenseSerializer,
            'DebtConfig': DebtSerializer,
            'TaxDeferredInvestmentConfig': TaxDeferredInvestmentSerializer,
            'BrokerageInvestmentConfig': BrokerageInvestmentSerializer,
            'IraInvestmentConfig': IraInvestmentSerializer,
        }
        return related_serializers.get(related_model.__name__)

    def create(self, validated_data):
        # Extract and process related ManyToMany fields
        many_to_many_fields = [
            ('cash_reserves', CashReserve),
            ('incomes', Income),
            ('expenses', Expense),
            ('debts', Debt),
            ('tax_deferred_investments', TaxDeferredInvestment),
            ('brokerage_investments', BrokerageInvestment),
            ('ira_investments', IraInvestment),
        ]

        related_objects = {}
        for field_name, related_model in many_to_many_fields:
            related_data = validated_data.pop(field_name, [])
            related_objects[field_name] = self.process_related_field(field_name, related_model, related_data)

        # Create the PlanConfig instance
        plan = super().create(validated_data)

        # Add related objects to ManyToMany fields
        for field_name, objects in related_objects.items():
            getattr(plan, field_name).set(objects)

        return plan

    def update(self, instance, validated_data):
        # Handle nested objects for updates
        many_to_many_fields = [
            ('cash_reserves', CashReserve),
            ('incomes', Income),
            ('expenses', Expense),
            ('debts', Debt),
            ('tax_deferred_investments', TaxDeferredInvestment),
            ('brokerage_investments', BrokerageInvestment),
            ('ira_investments', IraInvestment),
        ]

        related_objects = {}
        for field_name, related_model in many_to_many_fields:
            if field_name in validated_data:
                related_data = validated_data.pop(field_name)
                related_objects[field_name] = self.process_related_field(field_name, related_model, related_data)

        # Update the PlanConfig instance
        plan = super().update(instance, validated_data)

        # Update related objects in ManyToMany fields
        for field_name, objects in related_objects.items():
            getattr(plan, field_name).set(objects)

        return plan


class PlanTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanTemplate
        fields = '__all__'


class ManageRelatedModelSerializer(serializers.Serializer):
    related_model = serializers.CharField(max_length=255)
    related_id = serializers.IntegerField()
    action = serializers.ChoiceField(choices=['add', 'remove'])
