from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, is_admin=False, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            is_admin=is_admin,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        return self.create_user(
            email,
            is_admin=True,
            password=password,
        )


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=512, unique=True)
    full_name = models.TextField(max_length=512, blank=True)

    avatar = models.ImageField()

    joined_timestamp = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = EMAIL_FIELD = 'email'

    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_admin

    def get_full_name(self):
        return self.full_name

    def __str__(self):
        return f'{self.id} <{self.email}> {self.full_name}'.strip()
