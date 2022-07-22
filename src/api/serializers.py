from dataclasses import fields
from rest_framework import serializers
from app.models import User


class UserSerializer(serializers.ModelSerializer):
    address_count = serializers.UUIDField(required=False)
    class Meta:
        model = User
        fields = ("first_name", "last_name", "address_count")
