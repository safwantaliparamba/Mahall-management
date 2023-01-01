from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from customers.models import Customer
from api.v1.customers.serializers import CreateCustomerSerializer
from api.v1.general.functions import generate_serializer_errors


@api_view(['POST'])
@permission_classes([AllowAny])
def create_customer(request):
    print(request.POST)
    # customer = Customer.objects.create(request.POST, request.FILES)
    customer = CreateCustomerSerializer(data=request.data)
    
    if customer.is_valid():
        customer.save()

        response_data = {
            'statusCode':6000,
            'data': {
                "title":"Success",
                "message":"Customer created successfully",
            }
        }
    else:
        response_data = {
            'statusCode':6001,
            'data': {
                "title":"Failed",
                "message":generate_serializer_errors(customer._errors),
            }
        }
    return Response(response_data)