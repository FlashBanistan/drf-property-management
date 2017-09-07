from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from authentication.models import Tenant, TenantType, AuthUser

"""
GENERIC USER
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class AuthUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Password confirmation', required=False)

    class Meta:
        model = AuthUser
        fields = (
            'email',
            'is_superuser',
            'is_admin',
            'is_staff',
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
        user = super(AuthUserCreationForm, self).save(commit=False)
        if self.cleaned_data["password1"]:
            user.set_password(self.cleaned_data["password1"])
        if (user.email == 'None'):
            print('YEPPP')
            user.email = None
        if commit:
            user.save()
        return user

class AuthUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    email = forms.EmailField()

    class Meta:
        model = AuthUser
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
        return self.initial["password"]


class AuthUserAdmin(ModelAdmin):
    form = AuthUserChangeForm
    add_form = AuthUserCreationForm
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
    # search_fields = ('email',)
    # ordering = ('email',)
    filter_horizontal = ()


"""
NOW REGISTER THEM
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Now register the new UserAdmin...
admin.site.register(AuthUser, AuthUserAdmin)
admin.site.register(Tenant)
admin.site.register(TenantType)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
