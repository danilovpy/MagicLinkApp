import random
import string
from django.core.mail import send_mail


def get_random_string():
    length = 20
    letters_and_digits = string.ascii_letters + string.digits
    result = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result


def send_magic_link(request, to_email, token):
    send_mail(
        "Your magic link",
        f"https://{request.get_host()}/home/token={token}",
        "MagicLinkCreationApp@gmail.com",
        [to_email],
    )