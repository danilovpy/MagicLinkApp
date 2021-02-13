from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser):
    count = models.IntegerField(default=0)
    token = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.email)

    objects = UserManager()
