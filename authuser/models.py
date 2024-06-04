from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN","Admin"
        USER = "USER", "User"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50,choices=Role.choices)

    def save(self, *arg, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*arg,**kwargs)