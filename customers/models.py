from django.db import models

from general.models import BaseModel
from houses.models import House


class Customer(BaseModel):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(default=18)
    mobile_number = models.CharField(max_length=20)
    house = models.ForeignKey(House,on_delete=models.CASCADE,related_name="customers",null=True,blank=True)
    address = models.TextField(null=True, blank=True)
    job = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="customers/profile/",blank=True, null=True)
    blood_group = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "customers_customer"
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering = ["name","age"]