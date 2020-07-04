from rest_framework.serializers import (
    ValidationError,
    CharField,
    HyperlinkedModelSerializer,
    HyperlinkedRelatedField,
    ListSerializer,
    EmailField,
)
from .models import User


class UserReadSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "url",
            "display_name",
            "email",
            "is_admin",
            "is_tenant",
        ]


class UserBulkCreateSerializer(ListSerializer):
    def create(self, validated_data):
        users = [User(**user) for user in validated_data]
        return User.objects.bulk_create(users)


class UserWriteSerializer(HyperlinkedModelSerializer):
    email = EmailField(default=None)
    confirm_password = CharField(write_only=True, default=None)

    class Meta:
        model = User
        list_serializer_class = UserBulkCreateSerializer
        fields = [
            "url",
            "email",
            "display_name",
            "is_admin",
            "is_tenant",
            "password",
            "confirm_password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(email=validated_data["email"],)
        if validated_data["password"] != validated_data["confirm_password"]:
            raise ValidationError("Passwords do no match.")
        user.set_password(validated_data["password"])
        user.save()
        return user

