from django.db.models.signals import post_save
from django.dispatch import receiver
from billing.models import Payment
from datetime import datetime 

@receiver(post_save, sender=Payment)
def save_user_profile(sender, instance, **kwargs):
    if instance.invoice.total_payments == instance.invoice.total_charges:
        instance.invoice.paid_in_full_on = datetime.now()
        instance.invoice.save()