"""
URL configuration for FilmProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from films.views import  display_homepage, CreateFilm,CreateDirector,FilmList,DirectorList,UpdateFilm
urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', display_homepage),
    path('add-film/', CreateFilm.as_view()),
    path('add-director/', CreateDirector.as_view()),
    path('all-film/', FilmList.as_view(),name="all-film"),
    path('all-director/', DirectorList.as_view(),name="all-director"),
    path('update-film/<int:pk>', UpdateFilm.as_view()),
]
