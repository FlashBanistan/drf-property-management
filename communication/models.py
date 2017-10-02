from django.db import models


class Announcement(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateField(auto_now_add=True)