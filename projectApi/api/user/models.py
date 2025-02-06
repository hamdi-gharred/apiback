from django.db import models
from django.contrib.auth.models import AbstractUser
class UserCustomer(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    def __str__(self):
        return self.email

# Create your models here.
