from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver

from main.models import Income, TaxDeferred, Debt, Command, Expense, Brokerage, Ira, \
    RothIra, CashReserve, Plan, CommandSequence, CommandSequenceCommand, Hsa

RELATED = {
    "Debt",
    "Expense",
    "Income",
    "TaxDeferred",
    "Brokerage",
    "Ira",
    "RothIra",
    "CashReserve",
    "Hsa",
}

RELATED_MODELS = {
    "debts": Debt,
    "expenses": Expense,
    "incomes": Income,
    "tax_deferreds": TaxDeferred,
    "brokerages": Brokerage,
    "iras": Ira,
    "roth_iras": RothIra,
    "cash_reserves": CashReserve,
    "hsas":Hsa,
}


@receiver(post_save, sender=Debt)
@receiver(post_save, sender=Expense)
@receiver(post_save, sender=Income)
@receiver(post_save, sender=TaxDeferred)
@receiver(post_save, sender=Brokerage)
@receiver(post_save, sender=Ira)
@receiver(post_save, sender=RothIra)
@receiver(post_save, sender=CashReserve)
@receiver(post_save, sender=Hsa)
def create_command_for_related_models(sender, instance, created, **kwargs):
    """ Creates a Command when a related model is created and adds it to the Plan’s CommandSequence """
    if created:
        content_type = ContentType.objects.get_for_model(instance)
        command = Command.objects.create(
            content_type=content_type,
            object_id=instance.id,
            action="process"
        )


@receiver(post_delete, sender=Income)
@receiver(post_delete, sender=Expense)
@receiver(post_delete, sender=Debt)
@receiver(post_delete, sender=CashReserve)
@receiver(post_delete, sender=Brokerage)
@receiver(post_delete, sender=Ira)
@receiver(post_delete, sender=RothIra)
@receiver(post_delete, sender=TaxDeferred)
@receiver(post_delete, sender=Hsa)
def delete_command_for_related_models(sender, instance, **kwargs):
    content_type = ContentType.objects.get_for_model(instance)
    Command.objects.filter(content_type=content_type, object_id=instance.id).delete()


@receiver(m2m_changed)
def handle_plan_association(sender, instance: Plan, action, pk_set, model, **kwargs):
    if not isinstance(instance, Plan) or model._meta.object_name not in RELATED:
        return
    content_type = ContentType.objects.get_for_model(model)
    if action == "post_add":
        sequences = CommandSequence.objects.filter(
            plan=instance,
        )
        if not sequences:
            sequences = [CommandSequence.objects.create(
                plan=instance,
                name=f"{instance.name} Commands")]

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
    elif action == "post_remove":
        sequences = CommandSequence.objects.filter(plan=instance)
        if not sequences:
            return
        commands = Command.objects.filter(content_type=content_type, object_id__in=pk_set)
        CommandSequenceCommand.objects.filter(sequence__in=sequences, command__in=commands).delete()


@receiver(post_save, sender=Plan)
def add_initial_command_sequence_to_plan(instance: Plan, created: bool, **kwargs):
    plan = instance
    CommandSequence.objects.create(plan=plan, name=plan.name)


@receiver(post_save, sender=CommandSequence)
def add_commands_to_new_command_sequence(sender, instance: CommandSequence, created: bool, **kwargs):
    plan = instance.plan
    if created:
        max_order = instance.get_max_order()
        commands = []
        for related_attr, related_model_class in RELATED_MODELS.items():
            related_items = getattr(plan, related_attr)
            pk_set = related_items.values_list('pk')
            content_type = ContentType.objects.get_for_model(related_model_class)
            for command in Command.objects.filter(content_type=content_type, object_id__in=pk_set):
                commands.append(command)

        for command in commands:
            max_order += 1
            command_sequence_command, created = CommandSequenceCommand.objects.get_or_create(
                sequence=instance,
                command=command,
                order=max_order)
