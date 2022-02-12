from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): 
    username=models.CharField(max_length=30, unique=True)
    email=models.EmailField(unique=True, null=False)
    phone=models.CharField(max_length=30, null=True)
    first_name=models.CharField(max_length=30, null=True)
    last_name=models.CharField(max_length=30, null=True)

    class Meta:
        verbose_name="Usuário"
        verbose_name_plural="Usuários"
