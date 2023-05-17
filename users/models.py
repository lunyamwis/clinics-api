from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from roles.models import Role



class CustomUser(AbstractUser,PermissionsMixin):

    name = models.CharField(blank=True, max_length=255)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, 
                             null=True,blank=True)

    def __str__(self):
        return self.email
