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
    image=models.URLField()

class Rating(models.Model):
    film=models.ForeignKey(Film,on_delete=models.CASCADE,related_name='rating')
    stars=models.IntegerField()

class Comment(models.Model):
    film=models.ForeignKey(Film,on_delete=models.CASCADE,related_name='comment')
    comment=models.TextField()