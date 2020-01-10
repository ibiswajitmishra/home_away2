from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    CHOICES = (
        ('True', 'T'),
        ('False', 'F')
    )
    is_buyer = models.CharField(max_length=5, choices=CHOICES)

    def __str__(self):
        return self.username