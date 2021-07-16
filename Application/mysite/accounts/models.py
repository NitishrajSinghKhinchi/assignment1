from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username=None
    first_name=None
    last_name=None
    name=models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(_('email address'), unique=True)
    address = models.TextField(max_length=500)
    dateofbirth=models.DateField(null=True,blank=True)
    contact_number = models.CharField(null=True,blank=True,
                                      max_length=15,
                                      validators=[RegexValidator(r'^\d{3}\d{3}\d{4}$')],
                                      )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
