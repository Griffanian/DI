from typing import Any, Dict
from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import FilmForm, DirectorForm, AddPosterForm, AddRatingForm, AddCommentForm
from .models import Film,Director,Poster,Rating,Comment
from statistics import mean
import datetime


def display_homepage(request):

    return render(request,'index.html',{'films':Film.objects.all().order_by('title'),'directors':Director.objects.all().order_by('first_name')})

class FilmList(generic.ListView):

    template_name='all_films.html'
    context_object_name='items'
    model=Film

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['name'] = 'Films'
        return context

class DirectorList(generic.ListView):

    template_name='all_directors.html'
    context_object_name='items'
    model=Director

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['name'] = 'Directors'
        return context

class CreateFilm(LoginRequiredMixin, generic.CreateView):

    template_name='create.html'
    model=Film
    form_class=FilmForm
    success_url=reverse_lazy("all-film")

class CreatePoster(generic.CreateView):
    template_name='create.html'
    model=Poster
    form_class=AddPosterForm
    success_url=reverse_lazy("all-films")

class CreateDirector(generic.CreateView):

    template_name='create.html'
    model=Director
    form_class=DirectorForm
    success_url=reverse_lazy("all-director")


class ReadFilm(generic.detail.DetailView):
    context_object_name='item'
    model = Film
    template_name = 'display_film.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            ratings = int(round(mean([item.stars for item in Rating.objects.filter(film_id=context['item'].id)]),0))
            ratings = [i for i in range(ratings)]
            context['ratings'] = ratings
        except:
            pass
        context['comments']=[item.comment for item in Comment.objects.filter(film_id=context['item'].id)]
        return context

def add_rating(request, pk):
    film = Film.objects.get(id=pk)
    if request.method == 'POST':
        form = AddRatingForm(request.POST)
        if form.is_valid():
            film = form.cleaned_data['film']
            stars = form.cleaned_data['stars']
            rating = Rating.objects.create(film=film,stars=stars)
            rating.save()
            return redirect('/all-film/')
    else:
        form = AddRatingForm(initial={'film': film})
    return render(request, 'create.html', {'form': form, 'film': film})

def add_comment(request, pk):
    film = Film.objects.get(id=pk)
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            film = form.cleaned_data['film']
            comment = form.cleaned_data['comment']
            rating = Comment.objects.create(film=film,comment=comment)
            rating.save()
            return redirect('/all-film/')
    else:
        form = AddCommentForm(initial={'film': film})
    return render(request, 'create.html', {'form': form, 'film': film})

class ReadDirector(generic.detail.DetailView):
    context_object_name='item'
    model = Director
    template_name = 'display_director.html'

class UpdateFilm(generic.edit.UpdateView):

    model=Film
    fields = '__all__'
    template_name = 'create.html'
    success_url = 'all'

class UpdateDirector(generic.edit.UpdateView):

    model=Director
    fields = ['first_name','last_name']
    template_name = 'create.html'
    success_url = '/all-film/'
    
class DeleteFilm(generic.DeleteView):

    model=Film
    template_name = 'delete.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messages.add_message(self.request, messages.INFO, f"The film {self.get_object().title} has been deleted.")
        return context
    
class DeleteDirector(generic.DeleteView):
    
    model=Director
    template_name = 'delete.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messages.add_message(self.request, messages.INFO, f"The director {self.get_object()} has been deleted.")
        return context
    


