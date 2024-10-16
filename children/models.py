from uuid import uuid4

from django.db import models

from django.contrib.auth.models import User

class Child(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, blank=True)
    age = models.IntegerField(blank=True, null=True)
    months = models.IntegerField(blank=True, null=True)
    mother = models.ForeignKey(User, on_delete=models.CASCADE, related_name='children')



