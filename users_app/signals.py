from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Address, MyUser
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_adres(sender, instance, created, **kwargs):
    if created:
        Address.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_adres(sender, instance, **kwargs):
    instance.address.save()

