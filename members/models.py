from django.db import models

from general.models import BaseModel


class Member(BaseModel):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    member_id = models.CharField(max_length=30,default="MBID0")
    customer = models.OneToOneField('customers.Customer',on_delete=models.CASCADE,related_name="member")
    user = models.OneToOneField('users.User',on_delete=models.CASCADE,related_name="member",null=True,blank=True)
    encrypted_password = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "members_member"
        verbose_name = "Member"
        verbose_name_plural = "Members"
        ordering = ("name",)