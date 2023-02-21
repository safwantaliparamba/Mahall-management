# python imports 
import json
import base64
# from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.core import serializers
from django.core.files.base import ContentFile
# restframeworks imports 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
# local imports 
from houses.models import House
from customers.models import Customer
from general.decorators import group_required
from api.v1.general.paginator import Paginator
from general.functions import convert_base64_image_to_image
from api.v1.general.functions import generate_serializer_errors
from api.v1.customers.serializers import CustomerSerializer,CreateCustomerSerializer
from api.v1.general.http import HttpRequest


@api_view(['GET'])
@group_required(["chief"])
def get_customers(request:HttpRequest):

    if (customers:=Customer.objects.filter(is_deleted=False)).exists():
        customers = customers.order_by("-date_added")
        page = request.GET.get("page")
    
        paginated = Paginator(customers, 10,page)

        serialized = CustomerSerializer(
            paginated.objects,
            many=True,
            context={
                'request': request
            }
        ).data

        response_data = {
            "statusCode": 6000,
            "data": {
                "title": "Success",
                "current_page":paginated.current_page,
                "total_pages":paginated.total_pages,
                "total_items":paginated.total_items,
                "first_item":paginated.first_item,
                "last_item":paginated.last_item,
                "has_next":paginated.has_next_page,
                "has_previous":paginated.has_previous_page,
                "next_page":paginated.next_page_number,
                "previous_page":paginated.previous_page_number,
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
@group_required(["chief"])
def create_customer(request:HttpRequest):
    serialized = CreateCustomerSerializer(data=request.data)
    
    if serialized.is_valid():
        final_image = False
        name = serialized.data.get("name")
        image = serialized.data.get("image")

        if image and len(image) > 100:
            final_image = convert_base64_image_to_image(image,name)

        customer = Customer.objects.create(
            name=name,
            age=serialized.data.get("age"),
            mobile_number=serialized.data.get("mobile_number"),
            address=serialized.data.get("address"),
            job=serialized.data.get("job"),
            blood_group=serialized.data.get("blood_group"),
        )

        if final_image:
            customer.image = final_image
            customer.save()

        if  serialized.data.get("house_id") != None and House.objects.filter(id=serialized.data.get("house_id"),is_deleted=False).exists():
            house = House.objects.filter(id=serialized.data.get("house_id"),is_deleted=False).latest("date_added")
            customer.house = house
            
            customer.save()


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


@api_view(['POST'])
@group_required(["chief"])
def update_customer(request:HttpRequest, customer_id):
    
    if Customer.objects.filter(id=customer_id,is_deleted=False).exists():
        customer = Customer.objects.filter(id=customer_id,is_deleted=False).latest("date_added")
        serialized = CustomerSerializer(instance=customer,data=request.data,partial=True)

        if serialized.is_valid():
            image = request.data.get("image")
            name = serialized._validated_data.get("name", None)

            if image and len(image) > 100:
                final_image = convert_base64_image_to_image(image,name)
                serialized.save(image=final_image)
            else:
                serialized.save()    

            response_data = {
                "statusCode":6000,
                "data": {
                    "title": "Success",
                    "message": "Customer updated successfully",
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
    else:
        response_data = {
            "statusCode":6001,
            "data": {
                "title": "Failed",
                "message": "Customer not found",
            }
        }

    return Response(response_data,status=status.HTTP_200_OK)