from django import forms
from django.utils.safestring import mark_safe
from .models import Gif,Category

class GifForm(forms.ModelForm):
    uploader_name=forms.CharField(max_length=50,label=mark_safe('name'))
    title=forms.CharField(max_length=50,label=mark_safe('title'))
    url=forms.URLField(label=mark_safe('url'))
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),widget=forms.CheckboxSelectMultiple,label=mark_safe('categories'))
    class Meta:
        model = Gif
        fields = ['uploader_name','title','url','categories']
        exclude = ['likes']

class CategoryForm(forms.ModelForm):
    name=forms.CharField(max_length=50,label=mark_safe('name'))
    class Meta:
        model = Category
        fields = '__all__' 

class LikeForm(forms.Form):
    gif=forms.ModelChoiceField(queryset=Gif.objects.all())
    likes=forms.IntegerField()
    dislikes=forms.ModelChoiceField(queryset=Gif.objects.all())