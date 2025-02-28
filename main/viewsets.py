from django.contrib.auth import get_user_model
from django.db import transaction
from django.http import Http404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from common.utils.db_utils import get_many_to_many_fields
from .models import (
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
    TaxDeferredTemplate,
    Plan,
    PlanTemplate, RothIra, RothIraTemplate, CommandSequence, CommandSequenceCommand, Command,
)
from main.serializers import (
    BrokerageSerializer,
    BrokerageTemplateSerializer,
    CashReserveSerializer,
    CashTemplateSerializer,
    DebtSerializer,
    DebtTemplateSerializer,
    ExpenseSerializer,
    ExpenseTemplateSerializer,
    IncomeSerializer,
    IncomeTemplateSerializer,
    IraSerializer,
    IraTemplateSerializer,
    TaxDeferredSerializer,
    TaxDeferredTemplateSerializer,
    PlanSerializer,
    PlanTemplateSerializer, ManageRelatedModelSerializer, RothIraSerializer,
    RothIraTemplateSerializer, CommandSerializer, CommandSequenceSerializer,
    CommandSequenceCommandSerializer,
)

User = get_user_model()


class PlanRelatedViewSet(viewsets.ModelViewSet):
    """
    A generic viewset that auto-filters by `plan` when accessed under `/plans/<plan_id>/child/`
    and assigns `plan` automatically on create.
    """

    plan_lookup_field = 'plan_pk'
    plan_field_name = 'plan'

    def get_queryset(self):
        plan_id = self.kwargs.get(self.plan_lookup_field)
        if plan_id:
            return self.queryset.filter(**{self.plan_field_name: plan_id})
        return self.queryset

    def perform_create(self, serializer):
        plan_id = self.kwargs.get(self.plan_lookup_field)
        if plan_id:
            plan = get_object_or_404(self.get_queryset().model._meta.get_field(self.plan_field_name).related_model,
                                     id=plan_id)
            serializer.save(**{self.plan_field_name: plan})
        else:
            serializer.save()


class BrokerageViewSet(PlanRelatedViewSet):
    queryset = Brokerage.objects.all()
    serializer_class = BrokerageSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class BrokerageTemplateViewSet(PlanRelatedViewSet):
    queryset = BrokerageTemplate.objects.all()
    serializer_class = BrokerageTemplateSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class CashReserveViewSet(PlanRelatedViewSet):
    queryset = CashReserve.objects.all()
    serializer_class = CashReserveSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class CashReserveTemplateViewSet(PlanRelatedViewSet):
    queryset = CashReserveTemplate.objects.all()
    serializer_class = CashTemplateSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class DebtViewSet(PlanRelatedViewSet):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class DebtTemplateViewSet(PlanRelatedViewSet):
    queryset = DebtTemplate.objects.all()
    serializer_class = DebtTemplateSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class ExpenseViewSet(PlanRelatedViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class ExpenseTemplateViewSet(PlanRelatedViewSet):
    queryset = ExpenseTemplate.objects.all()
    serializer_class = ExpenseTemplateSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class IncomeViewSet(PlanRelatedViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class IncomeTemplateViewSet(PlanRelatedViewSet):
    queryset = IncomeTemplate.objects.all()
    serializer_class = IncomeTemplateSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class IraViewSet(PlanRelatedViewSet):
    queryset = Ira.objects.all()
    serializer_class = IraSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class IraTemplateViewSet(PlanRelatedViewSet):
    queryset = IraTemplate.objects.all()
    serializer_class = IraTemplateSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class RothIraViewSet(PlanRelatedViewSet):
    queryset = RothIra.objects.all()
    serializer_class = RothIraSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class RothIraTemplateViewSet(PlanRelatedViewSet):
    queryset = RothIraTemplate.objects.all()
    serializer_class = RothIraTemplateSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class TaxDeferredViewSet(PlanRelatedViewSet):
    queryset = TaxDeferred.objects.all()
    serializer_class = TaxDeferredSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)

    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)


class TaxDeferredTemplateViewSet(PlanRelatedViewSet):
    queryset = TaxDeferredTemplate.objects.all()
    serializer_class = TaxDeferredTemplateSerializer

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


class CommandViewSet(PlanRelatedViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer


class CommandSequenceViewSet(PlanRelatedViewSet):
    queryset = CommandSequence.objects.all()
    serializer_class = CommandSequenceSerializer


class CommandSequenceCommandViewSet(PlanRelatedViewSet):
    queryset = CommandSequenceCommand.objects.all()
    serializer_class = CommandSequenceCommandSerializer
