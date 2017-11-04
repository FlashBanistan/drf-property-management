from django.db import models
from users.models import Tenant


class Announcement(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

class MaintenanceRequest(models.Model):
    description = models.TextField()
    permission_to_enter = models.BooleanField(default=True)
    photo = models.FileField(null=True, blank=True, upload_to='maintenance_photos/')
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Tenant)