import uuid
from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=30, help_text="Enter application name")
    api_key = models.UUIDField(default=uuid.uuid4, editable=False)
