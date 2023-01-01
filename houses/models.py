import uuid

from django.db import models

from general.models import BaseModel


class House(BaseModel):
    id = models.UUIDField(unique=True,editable=False,default=uuid.uuid4)
    name = models.CharField(max_length=255)
    address = models.TextField()
    house_number = models.AutoField(primary_key=True,editable=False)
    mobile_number = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "houses_house"
        verbose_name = "house"
        verbose_name_plural = "houses"
        ordering = ("house_number","name")
