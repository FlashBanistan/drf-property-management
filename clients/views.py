from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from .models import Client
from .serializers import ClientSerializer


@method_decorator(user_passes_test(lambda u: u.is_superuser), name="dispatch")
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


def client_from_request(request):
    return request.user.client


class ClientAwareViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return super().get_queryset().filter(client=client_from_request(self.request))

    def perform_create(self, serializer, *args, **kwargs):
        client = client_from_request(self.request)
        serializer.save(client=client)
        super(ClientAwareViewSet, self).perform_create(serializer, *args, **kwargs)

