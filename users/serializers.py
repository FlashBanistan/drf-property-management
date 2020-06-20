from rest_framework.serializers import ValidationError, CharField, HyperlinkedModelSerializer, HyperlinkedRelatedField, ListSerializer, EmailField
from .models import Tenant, AuthUser, Admin


class AuthUserSerializer(HyperlinkedModelSerializer):
    email = EmailField(default=None)
    confirm_password = CharField(write_only=True, default=None)
    class Meta:
        model = AuthUser
        fields = [
            'url',
            'email',
            'password',
            'confirm_password'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        auth_user = AuthUser(
            email=validated_data['email'],
        )
        if validated_data['password'] != validated_data['confirm_password']:
            raise ValidationError("Passwords do no match.")
        auth_user.set_password(validated_data['password'])
        auth_user.save()
        return auth_user


class AdminSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Admin
        fields = [
            'url',
            'email',
        ]


class TenantBulkCreateSerializer(ListSerializer):
    def create(self, validated_data):
        tenants = [Tenant(**tenant) for tenant in validated_data]
        return Tenant.objects.bulk_create(tenants)


class TenantListSerializer(HyperlinkedModelSerializer):
    # auth = AuthUserSerializer(required=False, allow_null=True)
    class Meta:
        model = Tenant
        list_serializer_class = TenantBulkCreateSerializer
        fields = [
            'url',
            'first_name',
            'last_name',
            'dob',
            # 'phone_number',
            # 'ssn',
            # 'lease',
        ]


class TenantDetailSerializer(HyperlinkedModelSerializer):
    # auth = AuthUserSerializer(required=False, allow_null=True)
    class Meta:
        model = Tenant
        fields = [
            'url',
            'first_name',
            'last_name',
            'phone_number',
            'ssn',
            # 'lease',
            # 'complex',
            # 'building',
            # 'unit',
        ]