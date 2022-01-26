from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    family_id = models.ForeignKey(
        'accounts.Family',
        related_name='users',
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Family(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}'
