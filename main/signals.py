from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from main.models import Income, TaxDeferredInvestment, Debt, Command, Expense, BrokerageInvestment, IraInvestment, \
    RothIraInvestment, CashReserve


@receiver(post_save, sender=Debt)
@receiver(post_save, sender=Expense)
@receiver(post_save, sender=Income)
@receiver(post_save, sender=TaxDeferredInvestment)
@receiver(post_save, sender=BrokerageInvestment)
@receiver(post_save, sender=IraInvestment)
@receiver(post_save, sender=RothIraInvestment)
@receiver(post_save, sender=CashReserve)
def create_command_for_related_models(sender, instance, created, **kwargs):
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
    content_type = ContentType.objects.get_for_model(instance)
    Command.objects.filter(content_type=content_type, object_id=instance.id).delete()
