from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import DetailView,CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import generic
from .forms import CustomUserCreationForm, ProfileForm
from .models import UserProfile


def profile_redirect_view(request):
    
    user = request.user
    if hasattr(user,'profile'):
        return redirect('/')
    else:
        return redirect('create-profile')

def create_profile_view(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all-film')

    user = request.user
    form = ProfileForm(initial={'user': user})

    context = {'form': form}
    return render(request, 'create-profile.html',context)

class SignUpView(CreateView):

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        user = form.save()

        user.first_name = form.cleaned_data.get('first_name')
        user.last_name = form.cleaned_data.get('last_name')

        user.save()

        return super().form_valid(form)
    
@login_required
def profile_view(request):
    user = request.user
    date_joined = user.date_joined
    context = {'date_joined': date_joined}
    return render(request, 'profile.html' ,context)
