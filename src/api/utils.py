from app.models import User
from django.db.models import Count


def users_with_address_count():
    return (
        User.objects
        .values("uid", "first_name", "last_name")
        .annotate(address_count=Count("address"))
    )
