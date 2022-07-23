from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from app.models import User, Address
from ..serializers import UserSerializer, RecentAddressesSerializer
from app import database
from json import dumps


class GetUsersTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        user1 = User.objects.create(first_name="a", last_name="b", phone_number="+989000000000")
        user2 = User.objects.create(first_name="c", last_name="d", phone_number="+989000000001")
        self.user3 = User.objects.create(first_name="e", last_name="f", phone_number="+989000000002")

        Address.objects.create(user=user1, title="title1", latitude=34.765125, longitude=-12.45)
        Address.objects.create(user=user1, title="title2", latitude=44.267125, longitude=-12)
        Address.objects.create(user=user2, title="title1", latitude=34.765125, longitude=122)
        Address.objects.create(user=user2, title="title2", latitude=64.265175, longitude=2.543287)
        Address.objects.create(user=user2, title="title3", latitude=14.665135, longitude=87.4)
        return super().setUp()


    def test_add_address(self):
        address = {
            "user": str(self.user3.uid),
            "title": "a title for the address",
            "latitude": 78,
            "longitude": -23
        }

        create_response = self.client.post(
            "/api/add_address",
            dumps(address),
            content_type="application/json"
        )

        users = database.users_with_address_count()

        for user in users:
            user["recent_addresses"] = RecentAddressesSerializer(
                database.most_recent_addresses(user, 3),
                many=True
            ).data

        serializer = UserSerializer(users, many=True)

        response = self.client.get("/api/get_users?admin=true")

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
