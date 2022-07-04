from applications.user.models import User
from django.db import models
from djmoney.models.fields import MoneyField


# Create your models here.
class Charge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    monto = MoneyField(max_digits=14, decimal_places=2, default_currency='GTQ')

    def __str__(self):
        return f'CHARGE-{self.user.id}'
