from django.db import models
from clients.models import ClientAwareModel
from property_management.models import CommonModel


class Announcement(CommonModel, ClientAwareModel):
    title = models.CharField(max_length=255)
    body = models.TextField()
    # created_by = models.ForeignKey(Employee) // add this after an Employee model has been created.


class MaintenanceRequest(CommonModel, ClientAwareModel):
    MAINTENANCE_STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("COMPLETED", "Completed"),
    )
    description = models.TextField()
    permission_to_enter = models.BooleanField()
    photo = models.FileField(null=True, blank=True, upload_to="maintenance_photos/")
    status = models.CharField(
        choices=MAINTENANCE_STATUS_CHOICES, default="PENDING", max_length=12
    )
    date_completed = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey("users.User", on_delete=models.PROTECT)

