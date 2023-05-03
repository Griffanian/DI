from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from .views import *
from .forms import ProfileForm
urlpatterns = [
    path('login/',LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/',profile_view, name='profile-page'),
    path('signup/',SignUpView.as_view(), name='signup-page'),
    path('create_profile/',create_profile_view, name='create-profile'),
    path('profile-redirect/',profile_redirect_view,name='profile-redirect'),
]