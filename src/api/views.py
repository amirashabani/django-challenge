from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer, AddressSerializer, RecentAddressesSerializer
from app import database


class UsersAPI(APIView):
    def get(self, request):
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
            users = database.users_with_address_count()

            if addr:
                users = users.filter(**address_filter)

            for user in users:
                user["recent_addresses"] = RecentAddressesSerializer(
                    database.most_recent_addresses(user, 3),
                    many=True
                ).data
        else:
            users = database.all_users()

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class AddressAPI(APIView):
    def post(self, request):
        serializer = AddressSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
