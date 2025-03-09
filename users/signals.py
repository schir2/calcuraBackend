from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User, Profile


@receiver(post_save, sender=User)
def add_profile_to_new_user(created: bool, instance: User, **kwargs):
    if created:
        Profile.objects.create(user=instance)