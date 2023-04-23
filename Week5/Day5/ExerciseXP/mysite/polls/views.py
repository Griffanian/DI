from django.shortcuts import render
from django.http import HttpResponse
import json
with open('/Users/Miles/DI/Week5/Day5/ExerciseXP/mysite/polls/static/animals.json', 'r') as f:
        data = json.load(f)
        
name_list=[]
for item in data['animals']:
    name_list.append(item['name'])
    

def family(request,id):
    try:
        context = data['families'][id-1]
    except:
         return 'None'
    return render(request, 'posts/family.html', context)

def animal(request,id):
    context = data['animals'][id-1]
    return render(request, 'posts/animal.html', context)

def animals(request):
    context = {'names':' '.join(name_list)}
    return render(request, 'posts/animals.html', context)
