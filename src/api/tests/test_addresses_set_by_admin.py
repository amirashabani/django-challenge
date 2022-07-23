from django.test import TestCase
from app.models import User, Address
from app import database


class GetUsersTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create(first_name="a", last_name="b", phone_number="+989000000000")
        user2 = User.objects.create(first_name="c", last_name="d", phone_number="+989000000001")
        self.user3 = User.objects.create(first_name="e", last_name="f", phone_number="+989000000002")

        Address.objects.create(user=user1, title="title1", latitude=34.765125, longitude=-12.45, creator=Address.simple_user)
        Address.objects.create(user=user1, title="title2", latitude=44.267125, longitude=-12, creator=Address.simple_user)
        Address.objects.create(user=user2, title="title1", latitude=34.765125, longitude=122, creator=Address.simple_user)
        Address.objects.create(user=user2, title="title2", latitude=64.265175, longitude=2.543287, creator=Address.simple_user)
        Address.objects.create(user=user2, title="title3", latitude=14.665135, longitude=87.4, creator=Address.simple_user)
        return super().setUp()


    def test_addresses_set_by_admin(self):
        address = Address.objects.create(
            user=self.user3,
            title="new address",
            latitude=78.127329,
            longitude=170.274321,
            creator=Address.admin
        )

        query = database.addresses_set_by_admin()
        
        self.assertEqual(len(query), 1)
        self.assertEqual(query[0], address)
