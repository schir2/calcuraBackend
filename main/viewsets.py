from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from rest_framework import viewsets, response, status
from rest_framework.generics import get_object_or_404

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
    PlanTemplateSerializer, RothIraSerializer,
    RothIraTemplateSerializer, CommandSerializer, CommandSequenceSerializer,
    CommandSequenceCommandSerializer, HsaSerializer,
)
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
    PlanTemplate, RothIra, RothIraTemplate, CommandSequence, CommandSequenceCommand, Command, Hsa,
)

User = get_user_model()


def create_command_sequence_commands(plan_instance: Plan, pk_set, model):
    content_type = ContentType.objects.get_for_model(model)
    sequences = CommandSequence.objects.filter(
        plan=plan_instance,
    )
    if not sequences:
        sequences = [CommandSequence.objects.create(
            plan=plan_instance,
            name= f"{plan_instance.name} Commands")]

    for sequence in sequences:
        max_order = sequence.get_max_order()

        commands = Command.objects.filter(content_type=content_type, object_id__in=pk_set).select_related(
            'content_type')
        for command in commands:
            max_order += 1
            command_sequence_command, created = CommandSequenceCommand.objects.get_or_create(
                sequence=sequence,
                command=command,
                order=max_order
            )


class PlanRelatedViewSet(viewsets.ModelViewSet):
    """
    A generic viewset that auto-filters by `plan` when accessed under `/plans/<plan_id>/child/`
    and assigns `plan` automatically on create.
    """

    def get_model_name(self):
        name = self.get_queryset().model._meta.get_field(self.plan_field_name).field.attname
        return name

    plan_lookup_field = 'plan_pk'
    plan_field_name = 'plans'

    def get_queryset(self):
        plan_id = self.kwargs.get(self.plan_lookup_field)
        if plan_id:
            return self.queryset.filter(**{self.plan_field_name: plan_id})
        return self.queryset

    @transaction.atomic
    def perform_create(self, serializer):
        plan_id = self.kwargs.get(self.plan_lookup_field)
        obj = serializer.save()
        if plan_id:
            plan = get_object_or_404(Plan, pk=plan_id)
            obj.plans.add(plan)
            obj_pk = obj.pk
            obj_model_class = obj._meta.model
            create_command_sequence_commands(plan, {obj_pk}, obj_model_class)

        return super().perform_create(serializer)

    @transaction.atomic
    def perform_update(self, serializer):
        plan_id = self.kwargs.get(self.plan_lookup_field)
        obj = serializer.save()
        if plan_id:
            plan = get_object_or_404(Plan, pk=plan_id)
            obj.plans.add(plan)
            obj_pk = obj.pk
            obj_model_class = obj._meta.model
            create_command_sequence_commands(plan, {obj_pk}, obj_model_class)


    def destroy(self, request, *args, **kwargs):
        plan_id = self.kwargs.get(self.plan_lookup_field)
        if plan_id:
            plan = get_object_or_404(Plan, pk=plan_id)
            getattr(plan, self.get_model_name()).remove(*self.get_queryset())
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        return super().destroy(request, *args, **kwargs)


class BrokerageViewSet(PlanRelatedViewSet):
    queryset = Brokerage.objects.all()
    serializer_class = BrokerageSerializer

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class HsaViewSet(PlanRelatedViewSet):
    queryset = Hsa.objects.all()
    serializer_class = HsaSerializer

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
