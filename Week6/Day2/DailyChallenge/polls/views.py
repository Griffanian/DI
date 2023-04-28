from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Gif,Category
from .forms import GifForm, CategoryForm, LikeForm

def homepage(request):
    context = {'objects':Gif.objects.all()}
    return render(request,'index.html',context)

def new_gif(request):
    if request.method == 'POST':
        form = GifForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = GifForm

    context = {'form':form}
    return render(request,'form.html',context)

def new_cat(request):

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = CategoryForm
    context = {'form':form}
    return render(request,'form.html',context)

def display_cat(request,id):
    try:
        cat=Category.objects.get(id=id)
        cat1=cat.gifs.all()
        context={'objects':cat1,'name':cat}
        return render(request,'index.html',context)
    except:
        return render(request,'index.html',{'objects':[],'Name':'None'})
    

def display_gif(request,id):
    context={'item':Gif.objects.get(id=id)}
    return render(request,'cat_view.html',context)

def likes(request):

    if request.method == 'POST':
        likeform_submitted = LikeForm(request.POST)
        if likeform_submitted.is_valid():

            gif = likeform_submitted.cleaned_data['gif']
            like = likeform_submitted.cleaned_data['like']

            if like:
                gif.likes += 1
            else:
                gif.likes -= 1

            gif.save()

    gifs_all=Gif.objects.all().order_by('title', 'likes')
    
    like_forms=[LikeForm(initial=({'gif':gif_instance, 'like': True})) for gif_instance in gifs_all]
    dislike_forms=[LikeForm(initial=({'gif':gif_instance, 'like':False})) for gif_instance in gifs_all]

    gif_forms=list(zip(gifs_all,like_forms,dislike_forms))
    
    context={'gif_forms':gif_forms}
    return render(request,'likes.html',context)