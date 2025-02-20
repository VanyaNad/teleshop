from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Stores Telegram user details"""
    telegram_id = models.BigIntegerField(unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    is_bot = models.BooleanField(default=False)

    def __str__(self):
        return self.username if self.username else f"User {self.telegram_id}"
