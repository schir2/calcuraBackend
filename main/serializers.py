from rest_framework import serializers

from .models import (
    BrokerageInvestmentConfig,
    BrokerageInvestmentTemplate,
    CashConfig,
    CashTemplate,
    DebtConfig,
    DebtTemplate,
    ExpenseConfig,
    ExpenseTemplate,
    IncomeConfig,
    IncomeTemplate,
    IraInvestmentConfig,
    IraInvestmentTemplate,
    TaxDeferredInvestmentConfig,
    TaxDeferredInvestmentTemplate,
    PlanConfig,
    PlanTemplate,
)


class BrokerageInvestmentConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrokerageInvestmentConfig
        fields = '__all__'


class BrokerageInvestmentTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrokerageInvestmentTemplate
        fields = '__all__'


class CashConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashConfig
        fields = '__all__'


class CashTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashTemplate
        fields = '__all__'


class DebtConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebtConfig
        fields = '__all__'


class DebtTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebtTemplate
        fields = '__all__'


class ExpenseConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseConfig
        fields = '__all__'


class ExpenseTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseTemplate
        fields = '__all__'


class IncomeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeConfig
        fields = '__all__'


class IncomeTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeTemplate
        fields = '__all__'


class IraInvestmentConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = IraInvestmentConfig
        fields = '__all__'


class IraInvestmentTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IraInvestmentTemplate
        fields = '__all__'


class TaxDeferredInvestmentConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxDeferredInvestmentConfig
        fields = '__all__'


class TaxDeferredInvestmentTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxDeferredInvestmentTemplate
        fields = '__all__'


class PlanConfigSerializer(serializers.ModelSerializer):
    cashes = CashConfigSerializer(required=False, many=True)
    incomes = IncomeConfigSerializer(required=False, many=True)
    expenses = ExpenseConfigSerializer(required=False, many=True)
    debts = DebtConfigSerializer(required=False, many=True)
    tax_deferred_investments = TaxDeferredInvestmentConfigSerializer(required=False, many=True)
    brokerage_investments = BrokerageInvestmentConfigSerializer(required=False, many=True)
    ira_investments = IraInvestmentConfigSerializer(required=False, many=True)

    class Meta:
        model = PlanConfig
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
            'CashConfig': CashConfigSerializer,
            'IncomeConfig': IncomeConfigSerializer,
            'ExpenseConfig': ExpenseConfigSerializer,
            'DebtConfig': DebtConfigSerializer,
            'TaxDeferredInvestmentConfig': TaxDeferredInvestmentConfigSerializer,
            'BrokerageInvestmentConfig': BrokerageInvestmentConfigSerializer,
            'IraInvestmentConfig': IraInvestmentConfigSerializer,
        }
        return related_serializers.get(related_model.__name__)

    def create(self, validated_data):
        # Extract and process related ManyToMany fields
        many_to_many_fields = [
            ('cash', CashConfig),
            ('incomes', IncomeConfig),
            ('expenses', ExpenseConfig),
            ('debts', DebtConfig),
            ('tax_deferred_investments', TaxDeferredInvestmentConfig),
            ('brokerage_investments', BrokerageInvestmentConfig),
            ('ira_investments', IraInvestmentConfig),
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
            ('cash', CashConfig),
            ('incomes', IncomeConfig),
            ('expenses', ExpenseConfig),
            ('debts', DebtConfig),
            ('tax_deferred_investments', TaxDeferredInvestmentConfig),
            ('brokerage_investments', BrokerageInvestmentConfig),
            ('ira_investments', IraInvestmentConfig),
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
