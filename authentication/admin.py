from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from authentication.models import Tenant, TenantType, GenericUser

"""
GENERIC USER
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class GenericUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Password confirmation', required=False)

    class Meta:
        model = GenericUser
        fields = (
            'email',
            'is_superuser',
            'is_admin',
            'is_staff'
        )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(GenericUserCreationForm, self).save(commit=False)
        if self.cleaned_data["password1"]:
            user.set_password(self.cleaned_data["password1"])
        print('EMAILLLL:::::::: ', user.email)
        print('TYPE::: ', type(user.email))
        if (user.email == 'None'):
            print('YEPPP')
            user.email = None
        if commit:
            user.save()
        return user

class GenericUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    email = forms.EmailField()

    class Meta:
        model = GenericUser
        fields = (
            'email',
            'password',
            'is_superuser',
            'is_admin',
            'is_staff'
        )

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        print("CLEANING PASSWORD")
        return self.initial["password"]


class GenericUserAdmin(ModelAdmin):
    form = GenericUserChangeForm
    add_form = GenericUserCreationForm
    empty_value_display = 'unknown'

    list_display = ('email', 'is_superuser', 'is_admin', 'is_staff', )
    list_filter = ('is_superuser', 'is_admin', 'is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'is_superuser', 'is_admin', 'is_staff')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_superuser', 'is_admin', 'is_staff')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


"""
TENANT
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class TenantCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Password confirmation', required=False)

    class Meta:
        model = Tenant
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'ssn',
            'tenant_type',
        )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(TenantCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class TenantChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Tenant
        fields = (
            'email',
            'password',
            'first_name',
            'last_name',
            'phone_number',
            'ssn',
            'tenant_type',
        )

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class TenantAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = TenantChangeForm
    add_form = TenantCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    # list_display = ('email', 'is_admin')
    # list_filter = ('is_admin')
    list_display = ('email', 'first_name', 'last_name', 'id', 'is_admin', )
    list_filter = ('tenant_type', 'last_name', 'email')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'phone_number', 'ssn', 'tenant_type')}),
        # ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


"""
NOW REGISTER THEM
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Now register the new UserAdmin...
admin.site.register(Tenant, TenantAdmin)
admin.site.register(GenericUser, GenericUserAdmin)
admin.site.register(TenantType)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
