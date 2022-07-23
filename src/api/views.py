from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer, AddressSerializer, RecentAddressesSerializer
from app.models import User, Address
from django.db.models import Count


@api_view(["GET"])
def get_users(request):
    # is the request from admin?
    # /api/get_users?admin=true
    admin = request.query_params.get("admin", "false").lower() == "true"

    # filter based on number of addresses
    # /api/get_users?admin=true&addr=gt_5
    if addr := request.query_params.get("addr"):
        parts = addr.split("_")
        if len(parts) == 2:
            operator = parts[0]
            try:
                number = int(parts[1])
            except ValueError:
                addr = None
            else:
                if operator in ["eq", "ne", "lt", "lte", "gt", "gte"]:
                    address_filter = {f"address_count__{operator}": number}
                else:
                    addr = None
        else:
            addr = None

    if admin:
        users = (
            User.objects
            .values("uid", "first_name", "last_name")
            .annotate(address_count=Count("address"))
        )

        if addr:
            users = users.filter(**address_filter)

        for user in users:
            recent_addresses = (
                Address.objects
                .filter(user=user["uid"])
                .order_by("-created")
            )[:3]

            user["recent_addresses"] = RecentAddressesSerializer(recent_addresses, many=True).data
    else:
        users = User.objects.all()

    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_address(request):
    serializer = AddressSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
