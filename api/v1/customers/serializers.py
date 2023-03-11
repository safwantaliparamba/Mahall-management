from rest_framework import serializers

from customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    # image = serializers.CharField(max_length=1000000,required=False)

    class Meta:
        model = Customer
        fields = ('id', 'name','age','mobile_number','address','job','blood_group','image')
        read_only_fields = ['id','image']


class CreateCustomerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    age = serializers.CharField(max_length=10)
    mobile_number = serializers.CharField(max_length=128)
    job = serializers.CharField(max_length=128)
    image = serializers.CharField(max_length=1000000,required=False)
    blood_group = serializers.CharField(max_length=30)
    house_id = serializers.UUIDField(required=False)
