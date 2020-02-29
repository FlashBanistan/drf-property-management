from django.db import models
from django.utils import timezone
import uuid


class CommonModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
