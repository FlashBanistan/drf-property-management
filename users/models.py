from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager as DjBaseUserManager, PermissionsMixin)
# from model_utils.managers import InheritanceManager
from property_management.validators.phone_number import validate_phone_number
from property_management.models import CommonModel


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


class AuthUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True, blank=True, default=None)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = USERNAME_FIELD
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


class CommonUserModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Tenant(CommonModel, CommonUserModel):
    """
    A tenant is legally responsible for the terms of the lease.
    """
    phone_number = models.CharField(max_length=11, validators=[validate_phone_number])
    ssn = models.CharField(max_length=11, null=True, blank=True)
    # Relationships:
    auth = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    lease = models.ForeignKey('legal.Lease', related_name='tenants', on_delete=models.DO_NOTHING)
    # complex = models.ForeignKey('real_estate.Complex', null=True, blank=True, default=None, related_name='tenants')
    # building = models.ForeignKey('real_estate.Building', null=True, blank=True, default=None, related_name='tenants')
    # unit = models.ForeignKey('real_estate.Unit', null=True, blank=True, default=None, related_name='tenants')


class Occupant(CommonModel, CommonUserModel):
    """
    An occupant is anyone under the age of 18 and is NOT legally responsible for the lease.
    """
    lease = models.ForeignKey('legal.Lease', related_name='occupants', on_delete=models.DO_NOTHING)
    class Meta:
        pass
