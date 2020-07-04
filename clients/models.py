from django.db import models
import uuid


class Client(models.Model):
    # Identifaction details:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    # owner = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    # phone = models.CharField(max_length=11, validators=[validate_phone_number])
    # Location details:
    # address = models.CharField(max_length=100, null=False, blank=False)
    # city = models.CharField(max_length=100, null=False, blank=False)
    # state = models.CharField(max_length=100, null=False, blank=False)
    # zip_code = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.name


class ClientAwareModel(models.Model):
    client = models.ForeignKey("clients.Client", on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True
