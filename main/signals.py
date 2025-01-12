from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from main.models import Income, TaxDeferredInvestment


@receiver(pre_save, sender=TaxDeferredInvestment)
def post_tax_deferred_investment_saved(sender, instance, **kwargs):
    print(instance, 'pre save')

@receiver(post_save, sender=TaxDeferredInvestment)
def post_tax_deferred_investment_saved(sender, instance, **kwargs):
    print(instance, 'post save')