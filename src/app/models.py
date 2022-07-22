from django.db import models
from uuid import uuid4
from phonenumber_field.modelfields import PhoneNumberField


class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel):
    first_name = models.CharField("First name", max_length=150)
    last_name = models.CharField("Last name", max_length=150)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.uid})"


class Address(BaseModel):
    creator_choices = (
        (simple_user := "user", "user"),
        (admin := "admin", "admin"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="address")
    title = models.CharField("Title", max_length=150)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    creator = models.CharField(max_length=5, choices=creator_choices, default=simple_user)

    def __str__(self):
        return f"{self.latitude},{self.longitude} for {self.user} by {self.creator}"
