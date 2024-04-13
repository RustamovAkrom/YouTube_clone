from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.users.models import User
from django.core.mail import send_mail
from config import settings

MESSAGE = """
Hello World test
"""


@receiver(post_save, sender = User)
def remove_from_invertory(sender, instance, created, **kwargs):
    if created:
        print("sending email")
        print(settings.EMAIL_HOST_USER)
        print(instance.email)
        send_mail(
            subject = f"Welcome media sayt {instance.username}",
            message = MESSAGE,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [instance.email]
        )
