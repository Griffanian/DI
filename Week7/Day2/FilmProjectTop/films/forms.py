from django import forms
from .models import Film,Director,Poster

class FilmForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.DateInput())
    class Meta:
        model = Film
        fields = '__all__'
        widgets = {
            'release_date':forms.DateInput()
        }

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
    
class AddPosterForm(forms.Form):
    film = forms.ModelChoiceField(queryset=Film.objects.all(),widget=forms.HiddenInput())
    image = forms.URLField()

class AddRatingForm(forms.Form):
    CHOICES=[(1,1),(2,2),(3,3),(4,4),(5,5)]
    film = forms.ModelChoiceField(queryset=Film.objects.all(),widget=forms.HiddenInput())
    stars = forms.ChoiceField(choices=CHOICES)

class AddCommentForm(forms.Form):
    film = forms.ModelChoiceField(queryset=Film.objects.all(),widget=forms.HiddenInput())
    comment = forms.CharField(max_length=255)
    



