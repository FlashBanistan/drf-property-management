from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager as DjBaseUserManager)
from model_utils.managers import InheritanceManager
from property_management.validators.phone_number import validate_phone_number


class BaseUserManager(DjBaseUserManager, InheritanceManager):
    """
    Manager for all Users types
    create_user() and create_superuser() must be overriden as we do not use
    unique username but unique email.
    """

    def create_user(self, email=None, password=None, **extra_fields):
        now = timezone.now()
        email = BaseUserManager.normalize_email(email)
        u = GenericUser(email=email, is_superuser=False, last_login=now,
                        **extra_fields)
        u.set_password(password)
        u.save(using=self._db)
        return u

    def create_superuser(self, email, password, **extra_fields):
        u = self.create_user(email, password, **extra_fields)
        u.is_superuser = True
        u.is_admin = True
        u.is_staff = True
        u.save(using=self._db)
        return u


class CallableUser(AbstractBaseUser):
    """
    The CallableUser class allows to get any type of user by calling
    CallableUser.objects.get_subclass(email="my@email.dom") or
    CallableUser.objects.filter(email__endswith="@email.dom").select_subclasses()
    """
    email = models.EmailField(unique=True, default=None, null=True, blank=True)
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELD = USERNAME_FIELD
    objects = BaseUserManager()

    def __str__(self):
        return str(self.email)


class AbstractUser(CallableUser):
    """
    Here are the fields that are shared among specific User subtypes.
    Making it abstract makes 1 email possible in each User subtype.
    """
    is_superuser = False
    is_staff = False
    is_admin = False
    objects = BaseUserManager()

    def __str__(self):
        if (self.email is None):
            return ''
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app 'app_label'?"
        #Simplest possible answer: yes, always
        return True

    class Meta:
        abstract = True


class GenericUser(AbstractUser):
    """
    A GenericUser is any type of system user (such as an admin).
    This is the one that should be referenced in settings.AUTH_USER_MODEL
    """
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return str(self.email)


class TenantType(models.Model):
    name = models.CharField(max_length=100)
    numerical_order = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.numerical_order) + ' - ' + str(self.name)


class Tenant(GenericUser):
    """
    User subtype with specific fields and properties
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11, validators=[validate_phone_number], null=True, blank=True)
    ssn = models.CharField(max_length=11, null=True, blank=True)
    # Relationships:
    tenant_type = models.ForeignKey(TenantType, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        if (self.first_name is None or self.last_name is None):
            return ''
        return self.first_name + ' ' + self.last_name


