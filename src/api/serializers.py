from rest_framework import serializers
from app.models import User, Address


class UserSerializer(serializers.ModelSerializer):
    address_count = serializers.UUIDField(required=False)
    class Meta:
        model = User
        fields = ("first_name", "last_name", "address_count")


class AddressSerializer(serializers.ModelSerializer):
    creator = serializers.CharField(default=Address.admin, initial=Address.admin)


    class Meta:
        model = Address
        fields = ("user", "title", "latitude", "longitude", "creator")


    def to_representation(self, instance):
        self.fields["user"] = UserSerializer(read_only=True)
        return super().to_representation(instance)
