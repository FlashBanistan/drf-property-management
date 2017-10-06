from rest_framework.serializers import ValidationError, CharField, HyperlinkedModelSerializer, HyperlinkedRelatedField, ListSerializer, EmailField
from .models import Tenant, TenantType, AuthUser

class AuthUserSerializer(HyperlinkedModelSerializer):
    email = EmailField(default=None)
    confirm_password = CharField(write_only=True, default=None)
    password = CharField(default=None)
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

class TenantTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = TenantType
        fields = '__all__'

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
            # 'tenant_type',
            'first_name',
            'last_name',
            # 'phone_number',
            # 'ssn',
            'lease',
            # 'auth',
        ]

class TenantDetailSerializer(HyperlinkedModelSerializer):
    auth = AuthUserSerializer(required=False, allow_null=True)
    lease = 'legal.LeaseDetailSerializer(many=True)'
    class Meta:
        model = Tenant
        depth = 1
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'ssn',
            'tenant_type',
            'lease',
            'auth',
        ]