from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Film
from django.contrib import messages

# @receiver(post_delete, sender=Film)
# def send_delete_message(sender, instance, **kwargs):
#     message = f"The film {instance.title} has been deleted."
#     print(message)
#     messages.success(None, message)