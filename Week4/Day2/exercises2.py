# Exercise 1

class Family:

    def __init__(self,last_name,members) -> None:
        self.last_name=last_name
        self.members={ item['name']:item for item in members}
        

    def born(self,name,**kwargs):
        self.members.update({name:{key: value for key, value in kwargs.items()}})
        self.members[name].update({'name':name})
        print(f'congratulations to the {self.last_name} Family on their new born {name}')

    def is_18(self,name):
        try:    
            if self.members[name]['age'] >= 18:
                return True
            else:
                return False
        except KeyError:
            return f'{name} could not be found'
    def family_presentation(self):
        for item in self.members:
            print(item, self.last_name)

# Bloom=Family('Bloom',[{'name':'Michael','age':35,'gender':'Male','is_child':False}, {'name':'Sarah','age':32,'gender':'Female','is_child':False}])

# Bloom.family_presentation()

# Exercise 2

class TheIncredibles(Family):
    def use_power(self,name):
        if self.members[name]['age'] >= 18:
            print(self.members[name]['name']+' uses '+self.members[name]['power'])
        else: 
            raise ValueError("Person is too young to use power")
    
    def incredible_presentation(self):
        # super().family_presentation()
        for item in self.members.values():
            try:
                print(f"{item['name']}\n{item['incredible_name']}")
            except KeyError:
                print(item['name'],'does not have an incredible name')
            try:
                print(item['power'])
            except KeyError:
                print(item['name'],' does not have a power')
            print('')
incredi=TheIncredibles('Winsor',[
    {'name':'Michael','age':5,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
])

incredi.incredible_presentation()

incredi.born(name='Baby Jack', power='unknown')

incredi.incredible_presentation()