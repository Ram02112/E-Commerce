from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from core.models import Vendor

@receiver(post_save, sender=User)
def create_vendor_for_staff_user(sender, instance, created, **kwargs):
    if created and instance.is_staff:
        Vendor.objects.create(user=instance, title=instance.username)