from django.urls import path
from polls import views

urlpatterns = [
    path('people/<int:id>', views.peopleid),
    path('people/',views.people)
]
