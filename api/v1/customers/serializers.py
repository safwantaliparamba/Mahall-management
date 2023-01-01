from rest_framework import serializers

from customers.models import Customer


class CreateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = ('house',)