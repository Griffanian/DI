from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

def display_phone(request):
    objects=Person.objects.all().order_by('phone_number')
    context = {'objects':objects}
    return render(request,'posts/display_phone.html',context)

def display_name(request):
    objects=Person.objects.all().order_by('name')
    context = {'objects':objects}
    return render(request,'posts/display_name.html',context)

# def family(request,id):
#     try:
#         context = data['families'][id-1]
#     except:
#          return 'None'
#     return render(request, 'posts/family.html', context)

# def animal(request,id):
#     context = data['animals'][id-1]
#     return render(request, 'posts/animal.html', context)

# def animals(request):
#     context = {'phones':' '.join(name_list)}
#     return render(request, 'posts/animals.html', context)
