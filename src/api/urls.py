from getpass import getuser
from django.urls import path
from .views import get_user, add_address


urlpatterns = [
    path("get_user", get_user),
    path("add_address", add_address),
]