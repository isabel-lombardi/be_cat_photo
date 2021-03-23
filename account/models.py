from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    # will hold a One-To-One relationship with the existing User Model
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

