from django.db import models
import datetime,django
class Country(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class Film(models.Model):
    title=models.CharField(max_length=50)
    release_date=models.DateField(default=django.utils.timezone.now(), )
    created_in_country=models.ForeignKey('Country',on_delete=models.CASCADE,related_name='films_created')
    available_in_countries=models.ManyToManyField('Country',related_name='available_films')
    category=models.ManyToManyField(Category)
    director=models.ManyToManyField('Director')

    def __str__(self) -> str:
        return self.title
    
class Director(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"