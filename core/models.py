from django.db import models

# Create your models here.
from django.db import models


class Message(models.Model):
    client_id = models.CharField(max_length=199, null=True, blank=True)
    topic = models.CharField(max_length=199, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
