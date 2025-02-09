from django.contrib.auth import get_user_model
from django.db import transaction
from django.http import Http404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from common.utils.db_utils import get_many_to_many_fields
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
from .serializers import (
    BrokerageInvestmentSerializer,
    BrokerageInvestmentTemplateSerializer,
    CashReserveSerializer,
    CashTemplateSerializer,
    DebtSerializer,
    DebtTemplateSerializer,
    ExpenseSerializer,
    ExpenseTemplateSerializer,
    IncomeSerializer,
    IncomeTemplateSerializer,
    IraInvestmentSerializer,
    IraInvestmentTemplateSerializer,
    TaxDeferredInvestmentSerializer,
    TaxDeferredInvestmentTemplateSerializer,
    PlanSerializer,
    PlanTemplateSerializer, ManageRelatedModelSerializer, RothIraInvestmentSerializer,
    RothIraInvestmentTemplateSerializer, UserSerializer,
)


class BrokerageInvestmentViewSet(viewsets.ModelViewSet):
    queryset = BrokerageInvestment.objects.all()
    serializer_class = BrokerageInvestmentSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class BrokerageInvestmentTemplateViewSet(viewsets.ModelViewSet):
    queryset = BrokerageInvestmentTemplate.objects.all()
    serializer_class = BrokerageInvestmentTemplateSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class CashReserveViewSet(viewsets.ModelViewSet):
    queryset = CashReserve.objects.all()
    serializer_class = CashReserveSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class CashReserveTemplateViewSet(viewsets.ModelViewSet):
    queryset = CashReserveTemplate.objects.all()
    serializer_class = CashTemplateSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class DebtViewSet(viewsets.ModelViewSet):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class DebtTemplateViewSet(viewsets.ModelViewSet):
    queryset = DebtTemplate.objects.all()
    serializer_class = DebtTemplateSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class ExpenseTemplateViewSet(viewsets.ModelViewSet):
    queryset = ExpenseTemplate.objects.all()
    serializer_class = ExpenseTemplateSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class IncomeTemplateViewSet(viewsets.ModelViewSet):
    queryset = IncomeTemplate.objects.all()
    serializer_class = IncomeTemplateSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class IraInvestmentViewSet(viewsets.ModelViewSet):
    queryset = IraInvestment.objects.all()
    serializer_class = IraInvestmentSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class IraInvestmentTemplateViewSet(viewsets.ModelViewSet):
    queryset = IraInvestmentTemplate.objects.all()
    serializer_class = IraInvestmentTemplateSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class RothIraInvestmentViewSet(viewsets.ModelViewSet):
    queryset = RothIraInvestment.objects.all()
    serializer_class = RothIraInvestmentSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class RothIraInvestmentTemplateViewSet(viewsets.ModelViewSet):
    queryset = RothIraInvestmentTemplate.objects.all()
    serializer_class = RothIraInvestmentTemplateSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class TaxDeferredInvestmentViewSet(viewsets.ModelViewSet):
    queryset = TaxDeferredInvestment.objects.all()
    serializer_class = TaxDeferredInvestmentSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)

    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)


class TaxDeferredInvestmentTemplateViewSet(viewsets.ModelViewSet):
    queryset = TaxDeferredInvestmentTemplate.objects.all()
    serializer_class = TaxDeferredInvestmentTemplateSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)

    @action(detail=True, methods=['post'])
    def manage_related_model(self, request, pk=None):
        plan = self.get_object()

        serializer = ManageRelatedModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        related_model = validated_data['related_model']
        related_pk = validated_data['related_id']
        action = validated_data['action']

        if related_model not in get_many_to_many_fields(plan):
            raise Http404(f'{related_model} is not a valid related model for Plan')

        related_manager = getattr(plan, related_model)

        RelatedModel = related_manager.model

        try:
            related_instance = RelatedModel.objects.get(id=related_pk)
        except RelatedModel.DoesNotExist:
            raise Http404(f'{RelatedModel.__name__} with ID {related_pk} does not exist.')

        with transaction.atomic():
            if action == 'add':
                related_manager.add(related_instance)
                message = f"Successfully added {RelatedModel.__name__} with ID {related_pk} to {related_model}."
            elif action == 'remove':
                related_manager.remove(related_instance)
                message = f"Successfully removed {RelatedModel.__name__} with ID {related_pk} from {related_model}."

        plan.refresh_from_db()
        serialized_plan = self.get_serializer(plan)

        return Response(
            serialized_plan.data, status=200
        )


class PlanTemplateViewSet(viewsets.ModelViewSet):
    queryset = PlanTemplate.objects.all()
    serializer_class = PlanTemplateSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
