from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    ValidationError
)
from .models import Client

class ClientSerializer(ModelSerializer):
    confirm_domain_url = CharField(write_only=True)
    class Meta:
        model = Client
        fields = [
            'name',
            'schema_name',
            'domain_url',
            'created_on',
            'id',
            # Write only fields (won't be returned in the response):
            'confirm_domain_url',
        ]

    def validate(self, data):
        # Check that domain urls match:
        if data['domain_url'] != data['confirm_domain_url']:
            raise ValidationError('Domain urls do not match.')
        return data

    def create(self, validated_data):
        client = Client(
            name = validated_data['name'],
            schema_name = validated_data['schema_name'],
            domain_url = validated_data['domain_url'],
        )
        client.save()

        return client