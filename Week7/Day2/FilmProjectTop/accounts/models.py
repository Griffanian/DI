from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image=models.URLField(blank=True)

    def __str__(self) -> str:
        return f"{self.user.username}"
