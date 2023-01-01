import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(unique=True,primary_key=True,editable=False,default=uuid.uuid4)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        abstract = True