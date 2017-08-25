from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    ModelSerializer,
    CharField,
    ValidationError
)
from .models import Client


class ClientSerializer(HyperlinkedModelSerializer):
    confirm_domain_url = CharField(write_only=True)
    class Meta:
        model = Client
        fields = [
            'url',
            'name',
            'email',
            'phone',
            'schema_name',
            'domain_url',
            'created_on',
            # Write only fields (won't be returned in the response):
            'confirm_domain_url',
        ]

    def validate(self, data):
        # Check if domain_url is included and that domain urls do not match:
        if data.get('domain_url') is not None and data['domain_url'] != data['confirm_domain_url']:
            raise ValidationError('Domain urls do not match.')
        return data

    def create(self, validated_data):
        client = Client(
            name = validated_data['name'],
            email = validated_data['email'],
            phone = validated_data['phone'],
            schema_name = validated_data['schema_name'],
            domain_url = validated_data['domain_url'],
        )
        client.save()
        return client