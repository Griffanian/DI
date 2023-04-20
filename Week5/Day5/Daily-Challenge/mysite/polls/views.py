from django.shortcuts import render
people_list = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

def peopleid(request,id):
    people_list[id-1].update({'bool':True})
    context=people_list[id-1]
    return render(request, 'posts/people.html', context)

def people(request):
    names=[]
    people_list.sort(key=lambda person: person['age'])
    for i in range(1,len(people_list),1):
        try:
            names.append(people_list[i]['name'])
        except:
            pass
    names='\n'.join(names)
    people_list.insert(0,names)
    final=[]
    for item in people_list:
        try:
            for key,value in item.items():
                final.append(f"{key} : {value}")
        except:
            final.append(item)
    keys = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen']
    final_dict={keys[i]:item for i,item in enumerate(final)}
    context=final_dict
    return render(request, 'posts/people.html', context)