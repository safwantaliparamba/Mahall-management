from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128)
    password = serializers.CharField(max_length=128)


class CreateAdminSerializer(serializers.Serializer):
    member_id = serializers.UUIDField()
    email = serializers.EmailField()

class ResetPasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128)
    new_password = serializers.CharField(max_length=128)