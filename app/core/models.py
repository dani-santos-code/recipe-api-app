from django.db import models

"""These are the three modules necessary to customize/extend the User Model
whilst making use of some of the Django User features that comes out of the box
"""

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                       PermissionsMixin

# Backlash here used to skip lines to keep them short and easy to read


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        # normalize_email is a helper function that
        # comes with the BaseUserManager
        # Creates User model
        user.set_password(password)
        # user.set(password)is a helper function
        # that comes from the AbstractBaseUser
        user.save(using=self._db)
        # this is to support multiple dbs

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User Model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    # here we are creating a new UserManager for our object

    USERNAME_FIELD = 'email'

    # Note:
    # is_superuser is included as part of the PermissionsMixin
