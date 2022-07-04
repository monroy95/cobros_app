from django.db import models
from datetime import datetime  # , timedelta


class UserManager(models.Manager):
    def accounts_receivable(self):
        """Returns those users who apply to the programmed charge.
        """
        active = self.filter(active_until__gte=datetime.today())
        return active

    def validate_payment_data(self, id_user):
        """Validates if a user has a payment method.

        Args:
            id_user (str): user

        Returns:
            bool: True/False
        """
        probando = self.filter(id=id_user, credit_card_token__isnull=False).exists()
        return probando
