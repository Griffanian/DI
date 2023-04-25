from django.db import models
import datetime

class Gif(models.Model):
    title=models.CharField(max_length=50)
    url=models.URLField()
    uploader_name=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

class Category(models.Model):
    name=models.CharField(max_length=50)
    gifs=models.ManyToManyField(Gif)

    def __str__(self):
        return f"{self.name}"