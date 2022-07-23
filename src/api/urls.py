from getpass import getuser
from site import getusersitepackages
from django.urls import path
from .views import get_users, add_address


urlpatterns = [
    path("get_users", get_users),
    path("add_address", add_address),
]
