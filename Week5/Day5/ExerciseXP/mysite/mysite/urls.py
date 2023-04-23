from django.urls import path
from polls import views

urlpatterns = [
    path('family/<int:id>',views.family),
    path('animal/<int:id>',views.animal, name='animals_all'),
    path('animals/',views.animals, name='animal_specific') ]