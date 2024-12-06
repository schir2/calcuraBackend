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
    RetirementConfig,
    RetirementTemplate,
    TaxConfig,
    TaxTemplate,
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


class RetirementConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetirementConfig
        fields = '__all__'


class RetirementTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetirementTemplate
        fields = '__all__'


class TaxConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxConfig
        fields = '__all__'


class TaxTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxTemplate
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
    class Meta:
        model = PlanConfig
        fields = '__all__'


class PlanTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanTemplate
        fields = '__all__'
