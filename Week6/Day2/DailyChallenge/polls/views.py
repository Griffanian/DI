from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Gif,Category
from .forms import GifForm, CategoryForm, LikeForm

def homepage(request):
    context = {'objects':Gif.objects.all()}
    return render(request,'index.html',context)

def new_gif(request):
    submitted=False
    if request.method == 'POST':
        form = GifForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/new_gif?submitted=True')
    else:
        form = GifForm
        if 'submitted' in request.GET:
            submitted = True

    context = {'form':form,'submitted':submitted}
    return render(request,'form.html',context)

def new_cat(request):
    submitted=False
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/new_cat?submitted=True')
    else:
        form = CategoryForm
        if 'submitted' in request.GET:
            submitted = True

    context = {'form':form,'submitted':submitted}
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
    gifs_all=Gif.objects.all()
    like_dislike_forms=[LikeForm(initial=({'gif':gif_instance})) for gif_instance in gifs_all]
    gif_forms=list(zip(gifs_all,like_dislike_forms))
    
    return render(request,'likes.html',context)