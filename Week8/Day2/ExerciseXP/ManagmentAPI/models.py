from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50)
    decription = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}"
    
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='employees')

    def __str__(self) -> str:
        return f"{self.name}"
    
class Project(models.Model):
    name = models.CharField(max_length=50)
    decription = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    employees = models.ManyToManyField(Employee,related_name='projects')

    def __str__(self) -> str:
        return f"{self.name}"
    
class Task(models.Model):
    name = models.CharField(max_length=50)
    decription = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField()
    project = models.ForeignKey(Project,on_delete=models.DO_NOTHING,related_name='tasks')

    def __str__(self) -> str:
        return f"{self.name}"