from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager as DjBaseUserManager,
    PermissionsMixin,
)

# from model_utils.managers import InheritanceManager
from property_management.validators.phone_number import validate_phone_number
from property_management.models import CommonModel
from clients.models import ClientAwareModel, Client


class BaseUserManager(DjBaseUserManager):
    """
    Manager for all Users types
    create_user() and create_superuser() must be overriden as we do not use
    unique username but unique email.
    """

    def create_user(self, email=None, password=None, client=None, **extra_fields):
        now = timezone.now()
        email = BaseUserManager.normalize_email(email)
        u = User(
            email=email,
            client=client,
            is_superuser=False,
            is_admin=False,
            is_tenant=False,
            last_login=now,
            **extra_fields
        )
        u.set_password(password)
        u.save(using=self._db)
        return u

    def create_tenant_user(
        self, email=None, password=None, client=None, **extra_fields
    ):
        u = self.create_user(email, password, client, **extra_fields)
        u.is_tenant = True
        u.save()
        return u

    def create_admin_user(self, email=None, password=None, client=None, **extra_fields):
        u = self.create_user(email, password, client, **extra_fields)
        u.is_admin = True
        u.save()
        return u

    def create_superuser(self, email, password, **extra_fields):
        clients = Client.objects.bulk_create(
            [Client(name="Superuser Client", email="superuser@gmail.com")]
        )
        client = Client.objects.get(email="superuser@gmail.com")
        extra_fields.update(client=client)
        u = self.create_user(email, password, **extra_fields)
        u.is_superuser = True
        u.is_admin = True
        u.is_tenant = True
        u.save()
        return u


class User(AbstractBaseUser, PermissionsMixin, ClientAwareModel):
    email = models.EmailField(unique=True, null=True, blank=True, default=None)
    display_name = models.CharField(blank=True, max_length=100)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_tenant = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELD = USERNAME_FIELD
    objects = BaseUserManager()

    def __str__(self):
        if self.email is None:
            return ""
        return self.email


class CommonUserModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.first_name + " " + self.last_name


class Occupant(CommonModel, CommonUserModel, ClientAwareModel):
    """
    An occupant is anyone under the age of 18 and is NOT legally responsible for the lease.
    """

    lease = models.ForeignKey(
        "legal.Lease", related_name="occupants", on_delete=models.DO_NOTHING
    )

    class Meta:
        pass
