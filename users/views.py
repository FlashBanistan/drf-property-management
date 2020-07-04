from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from clients.views import ClientAwareViewSet
from .serializers import (
    UserReadSerializer,
    UserWriteSerializer,
)
from .models import User


class UserViewSet(ClientAwareViewSet):
    queryset = User.objects.all()
    filter_fields = ("email",)
    ordering_fields = ("email",)
    search_fields = ("email",)

    def get_serializer_class(self):
        if self.action == "update" or self.action == "create":
            return UserWriteSerializer
        return UserReadSerializer

    @action(methods=["post"], detail=False)
    def bulk_create(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
