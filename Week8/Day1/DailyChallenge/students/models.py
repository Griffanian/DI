from django.db import models

from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    date_joined = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
