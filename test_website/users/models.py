from django.contrib.auth.models import AbstractUser
from django.db import models

from users.choices import EXPERIENCE_TYPES


# Create your models here.
class User(AbstractUser):
    is_customer = models.BooleanField(default=True, verbose_name='Является ли заказчиком?')

    about = models.CharField(max_length=1000, blank=True, verbose_name='О себе')

    experience = models.CharField(blank=True, verbose_name='Опыт работы',
                                  choices=EXPERIENCE_TYPES)

    telegram = models.CharField(blank=True, verbose_name='Telegram')