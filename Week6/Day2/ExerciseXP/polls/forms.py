from django import forms
from django.utils.safestring import mark_safe
from .models import Gif,Category

# class GifForm(forms.Form):
#     uploader_name=forms.CharField(max_length=50,label=mark_safe('<br /> name'))
#     title=forms.CharField(max_length=50,label=mark_safe('<br /> title'))
#     url=forms.URLField(label=mark_safe('<br /> url'))
#     categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),widget=forms.CheckboxSelectMultiple,label=mark_safe('<br /> categories'))

class GifForm(forms.ModelForm):
    uploader_name=forms.CharField(max_length=50,label=mark_safe('<br /> name'))
    title=forms.CharField(max_length=50,label=mark_safe('<br /> title'))
    url=forms.URLField(label=mark_safe('<br /> url'))
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),widget=forms.CheckboxSelectMultiple,label=mark_safe('<br /> categories'))
    class Meta:
        model = Gif
        fields = '__all__' 

class CategoryForm(forms.ModelForm):
    name=forms.CharField(max_length=50,label=mark_safe('<br /> name'))
    class Meta:
        model = Category
        fields = '__all__' 
