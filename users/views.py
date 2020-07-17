from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
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


@api_view(["POST"])
@permission_classes([])
def obtain_token_admin(request):
    if request.method == "POST":
        email = request.data.get("email")
        password = request.data.get("password")
        user = None
        if email and password:
            user = authenticate(email=email, password=password)
        if not user or not user.is_admin:
            return Response(data=None, status=status.HTTP_400_BAD_REQUEST)
        refresh = RefreshToken.for_user(user)
        return Response({"refresh": str(refresh), "access": str(refresh.access_token)})


@api_view(["POST"])
@permission_classes([])
def obtain_token_tenant(request):
    if request.method == "POST":
        email = request.data.get("email")
        password = request.data.get("password")
        user = None
        if email and password:
            user = authenticate(email=email, password=password)
        if not user or not user.is_tenant:
            return Response(data=None, status=status.HTTP_400_BAD_REQUEST)
        refresh = RefreshToken.for_user(user)
        return Response({"refresh": str(refresh), "access": str(refresh.access_token)})
