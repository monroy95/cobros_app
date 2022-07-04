import uuid
from django.db import models
from .managers import UserManager


# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    referral_code = models.UUIDField(default=uuid.uuid4, editable=False)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, null=True, blank=True)
    credit_card_token = models.CharField(max_length=50, null=True, blank=True)
    active_until = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    def __str__(self):
        return f"{self.id} - {self.first_name}"
