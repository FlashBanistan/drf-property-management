from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from datetime import datetime
from users.models import Tenant, Admin, AuthUser
from clients.models import Client


## TENANT SIGNALS ###
@receiver(post_save, sender=Tenant)
def create_auth_user_for_tenant(sender, instance, created, **kwargs):
    if created:
        try:
            AuthUser.objects.create_user(
                email=instance.email, client=instance.client, password="admin123",
            )
        except:
            instance.delete()


@receiver(post_delete, sender=Tenant)
def delete_auth_user_for_tenant(sender, instance, **kwargs):
    AuthUser.objects.get(email=instance.email).delete()


### ADMIN SIGNALS ###
@receiver(post_save, sender=Admin)
def create_auth_user_for_admin(sender, instance, created, **kwargs):
    if created:
        try:
            AuthUser.objects.create_admin_user(
                email=instance.email, password="admin123", client=instance.client
            )
        except:
            instance.delete()


@receiver(post_delete, sender=Admin)
def delete_auth_user_for_admin(sender, instance, **kwargs):
    AuthUser.objects.get(email=instance.email).delete()


## CLIENT SIGNALS ##
@receiver(post_save, sender=Client)
def create_admin_for_client(sender, instance, created, **kwargs):
    if created:
        try:
            Admin.objects.create(email=instance.email, client=instance)
        except:
            instance.delete()

