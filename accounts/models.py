import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from encrypted_id.models import EncryptedIDModel

from JASIRI_SIMULATION_TEST.metadata import MetaData


class User(AbstractUser, MetaData):
    has_set_password = models.BooleanField(default=False)
    role = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=False, unique=True, null=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, blank=False, null=False)
    has_reset_password = models.BooleanField(default=False)
    phone = models.CharField(max_length=13,blank=False,null=False,unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username",
                       )

    class Meta:
        db_table = "users"

