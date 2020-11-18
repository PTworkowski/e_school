from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Address, MyUser


@receiver(post_save, sender=MyUser)
def create_adres(sender, instance, created, **kwargs):
    if created:
        Address.objects.create(user=instance)


@receiver(post_save, sender=MyUser)
def save_adres(sender, instance, **kwargs):
    instance.address.save()
