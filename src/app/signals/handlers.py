from django.db.models.signals import post_save
from django.dispatch import receiver
from app.models import Address


@receiver(post_save, sender=Address)
def send_notif(sender, **kwargs):
    print("Notify")
