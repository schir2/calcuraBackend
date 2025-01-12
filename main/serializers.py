from rest_framework import serializers


class IncomeOrIdField(serializers.BaseSerializer):
    def to_internal_value(self, data):
        if isinstance(data, int):
            # Existing object by ID
            try:
                return Income.objects.get(id=data)
            except Income.DoesNotExist:
                raise serializers.ValidationError(
                    f"Income with ID {data} does not exist."
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
    income = IncomeOrIdField(required=False, many=False, )

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
    roth_ira_investments = RothIraInvestmentSerializer(required=False, many=True)

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
            'CashReserve': CashReserveSerializer,
            'Income': IncomeSerializer,
            'Expense': ExpenseSerializer,
            'Debt': DebtSerializer,
            'TaxDeferredInvestment': TaxDeferredInvestmentSerializer,
            'BrokerageInvestment': BrokerageInvestmentSerializer,
            'IraInvestment': IraInvestmentSerializer,
            'RothIraInvestment': RothIraInvestmentSerializer,
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
            ('roth_ira_investments', RothIraInvestment),
        ]

        related_objects = {}
        for field_name, related_model in many_to_many_fields:
            related_data = validated_data.pop(field_name, [])
            related_objects[field_name] = self.process_related_field(field_name, related_model, related_data)

        # Create the PlanConfig instance
        plan = super().create(validated_data)

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
            ('roth_ira_investments', RothIraInvestment),
        ]

        related_objects = {}
        for field_name, related_model in many_to_many_fields:
            if field_name in validated_data:
                related_data = validated_data.pop(field_name)
                related_objects[field_name] = self.process_related_field(field_name, related_model, related_data)

        plan = super().update(instance, validated_data)

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
