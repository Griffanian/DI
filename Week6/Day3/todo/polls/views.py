from django.shortcuts import render
from .models import Category,Todo
from .form import TodoForm
from django.http import HttpResponse

def todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            details=form.cleaned_data['details']
            deadline_date=form.cleaned_data['deadline_date']
            category=form.cleaned_data['category']
            HttpResponse('List has been created')
            Todo.objects.create(
                title=title,
                details=details,
                deadline_date=deadline_date,
                category=category,
            )
    else:
        form=TodoForm
    return render(request,'new.html',{'form':form})

def display_all(request):
    return render(request,'index.html',{'objects':Todo.objects.all()})
