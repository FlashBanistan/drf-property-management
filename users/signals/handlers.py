from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from datetime import datetime
from users.models import User
from clients.models import Client


## CLIENT SIGNALS ##
@receiver(post_save, sender=Client)
def create_admin_user_for_client(sender, instance, created, **kwargs):
    if created:
        try:
            User.objects.create_admin_user(
                email=instance.email, password="admin123", client=instance
            )
        except:
            instance.delete()

