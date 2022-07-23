from django.urls import path
from .views import UsersAPI, AddressAPI


urlpatterns = [
    path("get_users", UsersAPI.as_view()),
    path("add_address", AddressAPI.as_view()),
]
