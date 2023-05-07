from django.db import models
from django.contrib.auth.models import User
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
    release_date=models.DateField(default=django.utils.timezone.now())
    created_in_country=models.ForeignKey('Country',on_delete=models.CASCADE,related_name='films_created')
    available_in_countries=models.ManyToManyField('Country',related_name='available_countries')
    category=models.ManyToManyField(Category,related_name='related_category')
    director=models.ManyToManyField('Director',related_name='related_films')

    def __str__(self) -> str:
        return self.title
    
class Director(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
class Poster(models.Model):
    film=models.ForeignKey(Film,on_delete=models.CASCADE,related_name='poster')
    image=models.URLField()

class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,related_name='rating',null=True,blank=True)
    film=models.ForeignKey(Film,on_delete=models.CASCADE,related_name='rating')
    stars=models.IntegerField()

    def get_range(self):
        return range(self.stars)

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,related_name='comment',null=True,blank=True)
    film=models.ForeignKey(Film,on_delete=models.CASCADE,related_name='comment')
    comment=models.TextField()