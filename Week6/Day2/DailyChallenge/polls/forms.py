from django import forms
from django.utils.safestring import mark_safe
from .models import Gif,Category

class GifForm(forms.ModelForm):
    class Meta:
        model = Gif
        fields = ['uploader_name','title','url','categories']
        exclude = ['likes']
        
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.Textarea(attrs={'class': 'my_textarea'})
        } 

class LikeForm(forms.Form):

    gif=forms.ModelChoiceField(queryset=Gif.objects.all(), widget=forms.HiddenInput)
    like=forms.BooleanField(required=False, widget=forms.HiddenInput)
    