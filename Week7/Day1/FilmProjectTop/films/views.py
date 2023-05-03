from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.views.decorators.cache import never_cache
from .models import Film,Director
from .forms import AddFilmForm, AddDirectorForm


def display_homepage(request):
    return render(request,'index.html',{'films':Film.objects.all(),'directors':Director.objects.all()})

class FilmList(generic.ListView):
    # all = Film.objects.all()
    # all.delete()

    template_name='all.html'
    context_object_name='items'
    model=Film

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['name'] = 'Films'
        return context

class DirectorList(generic.ListView):

    template_name='all.html'
    context_object_name='items'
    model=Director

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['name'] = 'Directors'
        return context

class CreateFilm(generic.CreateView):

    template_name='create.html'
    model=Film
    form_class=AddFilmForm
    success_url=reverse_lazy("all-films")

class CreateDirector(generic.CreateView):

    template_name='create.html'
    model=Director
    form_class=AddDirectorForm
    success_url=reverse_lazy("all-director")

class UpdateFilm(generic.UpdateView):

    model=Film
    fields=['title','release_date','created_in_country']




