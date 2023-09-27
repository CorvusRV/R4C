from django.core.mail import send_mail

from R4C.settings import EMAIL_HOST_USER


def email_message(model, version, email):
    message = f"""Добрый день!
Недавно вы интересовались нашим роботом модели {model}, версии {version}.
Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами"""

    send_mail('Робот',
              message,
              EMAIL_HOST_USER,
              [email],
              fail_silently=False)
