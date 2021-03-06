from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import JSONField


class CustomUser(AbstractUser):
    reg = RegexValidator(r"^[+]{0,1}[0-9]{10,12}", "Invalid Mobile Number")
    id = models.UUIDField(primary_key=True, default=uuid4)
    username = models.CharField(max_length=50, unique=False)
    phone = models.CharField(max_length=13, validators=[reg])
    email = models.EmailField(unique=True, blank=False)
    address = JSONField(null=True)
    first_name = None
    last_name = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "phone"]


# Create your models here.
