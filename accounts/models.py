from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class MyAccountManager(BaseUserManager):
    def create_user(self, email,  username, region, phone_number, first_name, last_name, password=None):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            region=region,
            phone_number=phone_number,
     
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,

        )

        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True  # Add this line to set is_superuser
        user.save(using=self._db)

        return user
    

REGIONS_CHOICES = [
    ('AR', 'Ashanti Region'),
    ('BA', 'Brong-Ahafo Region'),
    ('CR', 'Central Region'),
    ('ER', 'Eastern Region'),
    ('NR', 'Northern Region'),
    ('UE', 'Upper East Region'),
    ('UW', 'Upper West Region'),
    ('VR', 'Volta Region'),
    ('WR', 'Western Region'),
    ('GR', 'Greater Accra Region'),
]

class Account(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = PhoneNumberField(blank=True)
    region = models.CharField(max_length=2, choices=REGIONS_CHOICES, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)  # Add this line for is_superuser

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = MyAccountManager()

    def __str__(self):
        return self.email
