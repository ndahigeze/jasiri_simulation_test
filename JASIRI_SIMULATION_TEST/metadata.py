
from django.db import models
import uuid


class MetaData(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, blank=False, null=False)
    deleted_status = models.BooleanField(default=False)
    doneAt = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated_at = models.DateTimeField(auto_now_add=True, editable=True)
    done_by = models.CharField(editable=False, max_length=255)
    last_updated_by = models.CharField(editable=True, max_length=255)

    class Meta:
        abstract = True