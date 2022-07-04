from applications.charges.models import Charge
from applications.user.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings


def generate_payment(user, amount):
    """Records user payments for applicable users

    Args:
        user (str): user
        amount (float): amount

    Returns:
        bool: True/False
    """
    try:
        payment = Charge.objects.create(user=user, monto=amount)
        payment.save()
        return True, 'Success',

    except Exception as e:
        return False, e,


def charge(user=None, amount=0):
    """Validates if the user applies for a charge.

    Args:
        user (Object, optional): user. Defaults to None.
        amount (float, optional): amount. Defaults to 0.

    Returns:
        bool: True/False
    """
    have_payment_method = User.objects.validate_payment_data(id_user=user.id)

    if not have_payment_method:
        return False

    status_payment = generate_payment(user, amount)
    return status_payment[0]


def send_email(user=None, success=False):
    """Utility for sending e-mails

    Args:
        user (_type_, optional): _description_. Defaults to None.
        success (bool, optional): _description_. Defaults to False.
    """
    try:
        context = {
            'mail': user.email,
            'user': f'{user.first_name} {user.last_name}',
            'status': success
        }
        template = get_template('email.html')
        content = template.render(context)

        email = EmailMultiAlternatives(
            'Charge',
            'This is a Demo',
            settings.EMAIL_HOST_USER,
            [user.email],
        )

        email.attach_alternative(content, 'text/html')
        email.send()

    except Exception as e:
        with open('log-error-correo.txt', 'w') as f:
            f.write(str(e))


def process_charge():
    """Method executed by the scheduled task
    """
    consulta = User.objects.accounts_receivable()

    for x in consulta:
        status_transaction = charge(user=x, amount=100)
        send_email(user=x, success=status_transaction)
