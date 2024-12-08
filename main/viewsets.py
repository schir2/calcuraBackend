from rest_framework import viewsets

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
from .serializers import (
    BrokerageInvestmentConfigSerializer,
    BrokerageInvestmentTemplateSerializer,
    CashConfigSerializer,
    CashTemplateSerializer,
    DebtConfigSerializer,
    DebtTemplateSerializer,
    ExpenseConfigSerializer,
    ExpenseTemplateSerializer,
    IncomeConfigSerializer,
    IncomeTemplateSerializer,
    IraInvestmentConfigSerializer,
    IraInvestmentTemplateSerializer,
    TaxDeferredInvestmentConfigSerializer,
    TaxDeferredInvestmentTemplateSerializer,
    PlanConfigSerializer,
    PlanTemplateSerializer,
)


class BrokerageInvestmentConfigViewSet(viewsets.ModelViewSet):
    queryset = BrokerageInvestmentConfig.objects.all()
    serializer_class = BrokerageInvestmentConfigSerializer


class BrokerageInvestmentTemplateViewSet(viewsets.ModelViewSet):
    queryset = BrokerageInvestmentTemplate.objects.all()
    serializer_class = BrokerageInvestmentTemplateSerializer


class CashConfigViewSet(viewsets.ModelViewSet):
    queryset = CashConfig.objects.all()
    serializer_class = CashConfigSerializer


class CashTemplateViewSet(viewsets.ModelViewSet):
    queryset = CashTemplate.objects.all()
    serializer_class = CashTemplateSerializer


class DebtConfigViewSet(viewsets.ModelViewSet):
    queryset = DebtConfig.objects.all()
    serializer_class = DebtConfigSerializer


class DebtTemplateViewSet(viewsets.ModelViewSet):
    queryset = DebtTemplate.objects.all()
    serializer_class = DebtTemplateSerializer


class ExpenseConfigViewSet(viewsets.ModelViewSet):
    queryset = ExpenseConfig.objects.all()
    serializer_class = ExpenseConfigSerializer


class ExpenseTemplateViewSet(viewsets.ModelViewSet):
    queryset = ExpenseTemplate.objects.all()
    serializer_class = ExpenseTemplateSerializer


class IncomeConfigViewSet(viewsets.ModelViewSet):
    queryset = IncomeConfig.objects.all()
    serializer_class = IncomeConfigSerializer


class IncomeTemplateViewSet(viewsets.ModelViewSet):
    queryset = IncomeTemplate.objects.all()
    serializer_class = IncomeTemplateSerializer


class IraInvestmentConfigViewSet(viewsets.ModelViewSet):
    queryset = IraInvestmentConfig.objects.all()
    serializer_class = IraInvestmentConfigSerializer


class IraInvestmentTemplateViewSet(viewsets.ModelViewSet):
    queryset = IraInvestmentTemplate.objects.all()
    serializer_class = IraInvestmentTemplateSerializer


class TaxDeferredInvestmentConfigViewSet(viewsets.ModelViewSet):
    queryset = TaxDeferredInvestmentConfig.objects.all()
    serializer_class = TaxDeferredInvestmentConfigSerializer


class TaxDeferredInvestmentTemplateViewSet(viewsets.ModelViewSet):
    queryset = TaxDeferredInvestmentTemplate.objects.all()
    serializer_class = TaxDeferredInvestmentTemplateSerializer


class PlanConfigViewSet(viewsets.ModelViewSet):
    queryset = PlanConfig.objects.all()
    serializer_class = PlanConfigSerializer


class PlanTemplateViewSet(viewsets.ModelViewSet):
    queryset = PlanTemplate.objects.all()
    serializer_class = PlanTemplateSerializer
