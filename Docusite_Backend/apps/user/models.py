from typing import Iterable, Optional
import uuid

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class UserManager(BaseUserManager):
    def _create_user(self, username, email, first_name,last_name, password, is_staff, is_superuser, **extra_fields):
        print(password)
        user = self.model(
            username = username,
            email = email,
            first_name = first_name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, first_name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, first_name,last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, first_name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, first_name,last_name, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):

    # ROLES CHOICES
    ROL_SUPER_ADMIN = 'SU'
    ROL_ADMIN = 'AD'
    ROL_USER = 'US'
    ROLES = (
        (ROL_SUPER_ADMIN, 'SUPERADMIN'),
        (ROL_ADMIN, 'ADMIN'),
        (ROL_USER, 'USER')   
    )

    rol = models.CharField(choices= ROLES, max_length= 3, verbose_name= 'rol')
    uuid = models.UUIDField(db_index= True, default= uuid.uuid4, editable= False, unique= True)
    username = models.CharField(max_length = 255, unique = True)
    email = models.EmailField('email',max_length = 255, unique = True,)
    first_name = models.CharField('name', max_length = 255, null= False)
    last_name = models.CharField('last_name', max_length = 255, null = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False) 
    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name','last_name', 'rol']

    def __str__(self):
        return f'{self.username} {self.rol}'


