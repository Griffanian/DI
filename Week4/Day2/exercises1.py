# Exercise 1

# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# cats_list=[Bengal('cat1',4),Chartreux('cat2',5),Siamese('cat3',6)]

# sarah_pets = Pets([Cat('cat4',7),Cat('cat5',8)])
# cats_list.append(sarah_pets)

# for item in cats_list:
#     if type(item).__name__ in ['Bengal','Chartreux','Siamese']:
#         print(item.walk())
#     if type(item).__name__ == 'Pets':
#         item.walk()

# Exercise 2

class Dog:
    def __init__(self,name:str,age:int,weight:int) -> None:
        self.name=name
        self.age=age
        self.weight=weight

    def bark(self):
        return f'{self.name} is barking!'

    def run_speed(self):
        return self.weight/(self.age*10)

    def fight_num(self):
        return self.run_speed()*self.weight

    def fight(self,other_dog):
        if self.fight_num()>other_dog.fight_num():
            return f'{self.name} won the fight!.'
        else:
            return f'{other_dog.name} won the fight!.'

# dog1=Dog("dog1",10,50)
# dog2=Dog("dog2",8,60)
# dog3=Dog("dog3",12,40)

# print(dog1.fight(dog3))





