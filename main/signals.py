from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import models

from main.models import Income, TaxDeferredInvestment, Debt, Command, Expense, BrokerageInvestment, IraInvestment, \
    RothIraInvestment, CashReserve, CommandSequence, CommandSequenceCommand


@receiver(post_save, sender=Debt)
@receiver(post_save, sender=Expense)
@receiver(post_save, sender=Income)
@receiver(post_save, sender=TaxDeferredInvestment)
@receiver(post_save, sender=BrokerageInvestment)
@receiver(post_save, sender=IraInvestment)
@receiver(post_save, sender=RothIraInvestment)
@receiver(post_save, sender=CashReserve)

def create_command_for_related_models(sender, instance, created, **kwargs):
    """ Creates a Command when a related model is created and adds it to the Plan’s CommandSequence """
    if created:
        content_type = ContentType.objects.get_for_model(instance)
        command = Command.objects.create(
            content_type=content_type,
            object_id=instance.id,
            action="create"
        )

@receiver(post_delete, sender=Debt)
@receiver(post_delete, sender=Expense)
@receiver(post_delete, sender=Income)
@receiver(post_delete, sender=TaxDeferredInvestment)
@receiver(post_delete, sender=BrokerageInvestment)
@receiver(post_delete, sender=IraInvestment)
@receiver(post_delete, sender=RothIraInvestment)
@receiver(post_delete, sender=CashReserve)
def delete_command_for_debt(sender, instance, **kwargs):
    """ Deletes associated Commands when a Debt is deleted """
    content_type = ContentType.objects.get_for_model(instance)
    Command.objects.filter(content_type=content_type, object_id=instance.id).delete()