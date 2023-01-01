import requests
import json

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from users.models import User
from members.models import Member
from general.encryptions import encrypt
from general.functions import generate_unique_id, random_password

from api.v1.users.serializers import LoginSerializer, CreateAdminSerializer, ResetPasswordSerializer
from api.v1.general.functions import generate_serializer_errors, send_email


@api_view(['POST'])
@permission_classes([AllowAny])
def admin_login(request):
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():

        if User.objects.filter(username=serializer.data.get('username'), is_deleted=False).exists():
            user = User.objects.filter(username=serializer.data.get('username'), is_deleted=False).latest('date_joined')
            is_admin = user.is_admin

            if is_admin:
                protocol = "http://"

                if request.is_secure():
                    protocol = "https://"

                host = request.get_host()
                headers = {
                    "Content-Type": "application/json"
                }
                url = protocol + host + "/api/v1/users/auth/login/"
                
                data = {
                    "username": user.username,
                    "password": serializer.data.get('password'),
                }

                response = requests.post(url, headers=headers, data=json.dumps(data))

                if response.status_code == 200:
                    response_data = {
                        "statusCode":6000,
                        "data":{
                            "title": "Success",
                            "message":"Successfully logged in",
                            "username": user.username,
                            "access":response.json()["access"],
                            "refresh":response.json()["refresh"],
                        }
                    }

                else:
                    response_data = {
                        "statusCode": 6001,
                        "data":{
                            "title": "Error",
                            "message": "Something went wrong"
                        }
                    }      

            else:
                response_data = {
                    "statusCode":6001,
                    "data": {
                        "title": "Error",
                        "message": "You have no authorities to access this website"
                    }
                }

        else:
            response_data = {
                "statusCode": 6001,
                "data": {
                    "title": "validation Error",
                    "message": "User doesn't exists"
                }
            }

    else:
        response_data ={
            "statusCode": 6001,
            "data": {
                "title": "validation Error",
                "message":generate_serializer_errors(serializer._errors)
            }
        }

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def create_admin(request):
    serializer = CreateAdminSerializer(data=request.data)

    if serializer.is_valid():

        if Member.objects.filter(id=serializer.data.get("member_id"),is_deleted=False).exists():
            member = Member.objects.filter(id=serializer.data.get("member_id"),is_deleted=False).latest('date_added')

            if not User.objects.filter(member__id=member.id).exists():
                username = generate_unique_id(12)
                duplicate_username = User.objects.filter(username=username).exists()

                while duplicate_username:
                    username = generate_unique_id(12)
                    duplicate_username = User.objects.filter(username=username).exists()

                password = random_password(12)

                user = User.objects.create_user(
                    username=username,
                    password=password,
                    first_name=member.name,
                    email=serializer.data.get("email"),
                    is_admin=True
                )

                member.user = user
                member.encrypted_password = encrypt(password)
                member.save() 

                # send_email(
                #     to_address=user.email,
                #     subject="Auth credintials",
                #     content="You are an admin now",
                #     html_content=f"hii <h1>{member.name}</h1><p>your username {user.username} and password {password}</p>"
                # )

                response_data = {
                    "statusCode": 6000,
                    "data": {
                        "title": "Success",
                        "message": "Admin creation success",
                        "username": user.username,
                        "password": password
                    }
                }
                
            else:
                response_data = {
                "statusCode": 6001,
                "data": {
                    "title": "Error",
                    "message": "User already exists",
                }
            }

        else:
            response_data = {
                "statusCode": 6001,
                "data": {
                    "title": "Validation Error",
                    "message": "Member doesn't exist",
                }
            }

    else:
        response_data = {
            "statusCode": 6001,
            "data": {
                "title": "Validation Error",
                "message": generate_serializer_errors(serializer._errors),
            }
        }

    return Response(response_data,status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reset_password(request):
    serializer = ResetPasswordSerializer(data=request.data)

    if serializer.is_valid():
        user = request.user 
        is_password_ok = user.check_password(serializer.data.get('old_password'))

        if is_password_ok:
            user.set_password(serializer.data.get('new_password'))
            user.member.encrypted_password = encrypt(serializer.data.get('new_password'))

            user.save()
            user.member.save()

            response_data = {
                "statusCode":6000,
                "data": {
                    "title": "Success",
                    "message": "Password Changed Successfully",
                }
            }

        else:
            response_data = {
                "statusCode":6001,
                "data": {
                    "title": "Failed",
                    "message": "Invalid password",
                }
            }

    else:
        response_data = {
            "statusCode": 6001,
            "data": {
                "title": "Validation error",
                "message": generate_serializer_errors(serializer._errors)
            }
        }

    return Response(response_data,status=status.HTTP_200_OK)