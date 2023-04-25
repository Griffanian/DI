from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=50)
    image=models.URLField()

    def __str__(self) -> str:
        return self.name

class Todo(models.Model):
    title=models.CharField(max_length=50)
    details=models.CharField(max_length=200)
    has_been_done=models.BooleanField(default=False)
    date_creation=models.DateTimeField(auto_now_add=True)
    date_completion=models.DateTimeField(null=True)
    deadline_date=models.DateField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title

