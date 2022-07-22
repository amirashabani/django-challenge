from getpass import getuser
from django.urls import path
from .views import get_user


urlpatterns = [
    path("get_user", get_user),
]