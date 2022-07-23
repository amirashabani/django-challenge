from app.models import User, Address
from django.db.models import Count


def users_with_address_count():
    return (
        User.objects
        .values("uid", "first_name", "last_name")
        .annotate(address_count=Count("address"))
    )


def most_recent_addresses(user, n):
    return (
        Address.objects
        .filter(user=user["uid"])
        .order_by("-created")
    )[:n]


def all_users():
    return User.objects.all()
