from django.db import models
from property_management.models import CommonModel


class Announcement(CommonModel):
    title = models.CharField(max_length=255)
    body = models.TextField()
    # created_by = models.ForeignKey(Employee) // add this after an Employee model has been created.

class MaintenanceRequest(CommonModel):
    description = models.TextField()
    permission_to_enter = models.BooleanField()
    photo = models.FileField(null=True, blank=True, upload_to='maintenance_photos/')
    created_by = models.ForeignKey('users.Tenant', on_delete=models.PROTECT)