from rest_framework import serializers

from customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name','age','mobile_number','address','job','blood_group','image')


class CreateCustomerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    age = serializers.IntegerField()
    mobile_number = serializers.IntegerField()
    job = serializers.CharField(max_length=128)
    # image = serializers.ImageField(required=False)
    blood_group = serializers.CharField(max_length=30)
    house_id = serializers.UUIDField(required=False)