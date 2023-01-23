# python imports 
import json
# from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.core import serializers
# restframeworks imports 
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
# local imports 
from customers.models import Customer
from api.v1.customers.serializers import CustomerSerializer,CreateCustomerSerializer
from api.v1.general.functions import generate_serializer_errors, paginate_items
from houses.models import House


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_customers(request):
    if Customer.objects.filter(is_deleted=False).exists():
        customers = Customer.objects.filter(is_deleted=False).order_by("-date_added")
        page = request.GET.get("page")

        paginated_data = paginate_items(customers, 10, page=page)

        serialized = CustomerSerializer(
            paginated_data["data"],
            many=True,
            context={
                'request': request
            }
        ).data

        response_data = {
            "statusCode": 6000,
            "data": {
                "title": "Success",
                "paginated_data": paginated_data["paginated_data"],
                "data": serialized
            }
        }

    else:
        response_data = {
            "statusCode": 6001,
            "data": {
                "title": "Failed",
                "message": "Customers not found"
            }
        }

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_customer(request):
    serialized = CreateCustomerSerializer(data=request.data)

    print(request.data)

    if serialized.is_valid():
        customer = Customer.objects.create(
            name=serialized.data.get("name"),
            age=serialized.data.get("age"),
            mobile_number=serialized.data.get("mobile_number"),
            address=serialized.data.get("address"),
            job=serialized.data.get("job"),
            image=request.data.get("image"),
            blood_group=serialized.data.get("blood_group"),
        )

        if  serialized.data.get("house_id") != None and House.objects.filter(id=serialized.data.get("house_id"),is_deleted=False).exists():
            house = House.objects.filter(id=serialized.data.get("house_id"),is_deleted=False).latest("date_added")
            customer.house = house
            
            customer.save()

        # if serialized.data.get("image") != None:
        #     customer.image = serialized.data.get("image")


        response_data = {
            "statusCode": 6000,
            "data": {
                "title":"Success",
                "message":"Customer created successfully"
            }
        }
    
    else:
        response_data = {
            "statusCode":6001,
            "data": {
                "title": "Failed",
                "message": generate_serializer_errors(serialized._errors)
            }
        }

    return Response(response_data,status=status.HTTP_200_OK)