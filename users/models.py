from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager as DjBaseUserManager)
# from model_utils.managers import InheritanceManager
from property_management.validators.phone_number import validate_phone_number


class BaseUserManager(DjBaseUserManager):
    """
    Manager for all Users types
    create_user() and create_superuser() must be overriden as we do not use
    unique username but unique email.
    """

    def create_user(self, email=None, password=None, **extra_fields):
        now = timezone.now()
        email = BaseUserManager.normalize_email(email)
        u = AuthUser(email=email, is_superuser=False, last_login=now,
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


class AuthUser(AbstractBaseUser):
    email = models.EmailField(unique=True, null=True, blank=True, default=None)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = USERNAME_FIELD
    # is_superuser = False
    # is_staff = False
    # is_admin = False
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
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


class Tenant(models.Model):
    """
    User subtype with specific fields and properties
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # phone_number = models.CharField(max_length=11, validators=[validate_phone_number], null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    ssn = models.CharField(max_length=11, null=True, blank=True)
    # Relationships:
    auth = models.OneToOneField(AuthUser, null=True, blank=True, default=None)
    lease = models.ForeignKey('legal.Lease', null=True, blank=True, related_name='tenants')
    property = models.ForeignKey('real_estate.Complex', null=True, blank=True, default=None, related_name='tenants')
    building = models.ForeignKey('real_estate.Building', null=True, blank=True, default=None, related_name='tenants')
    unit = models.ForeignKey('real_estate.Unit', null=True, blank=True, default=None, related_name='tenants')

    def __str__(self):
        if (self.first_name is None or self.last_name is None):
            return ''
        return self.first_name + ' ' + self.last_name


