from django.contrib.auth.models import AbstractUser
from django_extensions.db.models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    def __str__(self):
        return f"{self.pk} | {self.username} | {self.email}"
