from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    is_customer = models.BooleanField(default=True)

    about = models.CharField(max_length=1000, blank=True)

    experience = models.CharField(blank=True)

    telegram = models.CharField(blank=True)