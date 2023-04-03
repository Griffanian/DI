# Exercise 1

# class Cat:

#     instances=[]

#     def __init__(self:str, cat_name:str, cat_age:int):
#         self.name = cat_name
#         self.age = cat_age
#         Cat.instances.append(self)
#     def __str__(self) -> str:
#         return self.name

# Sally = Cat('Sally', 5)
# Monty = Cat('Monty',10)
# Harry = Cat('Harry', 4)
# Shelly = Cat('Shelly',15)

# def oldest_cat():
#     oldest=Cat.instances[0]
#     for item in Cat.instances:
#         if item.age > oldest.age:
#             oldest=item
#     return oldest


# print(f'The oldest cat is {oldest_cat().name} and is {oldest_cat().age} years old.')

# Exercise 2

# class Dog:
    
#     instances=[]

#     def __init__(self, dog_name:str, dog_height:int) -> None:
#         self.name=dog_name
#         self.height=dog_height
#         Dog.instances.append(self)

#     def bark(dog_name):

#         print(f'{dog_name} goes "Woof!"')
        
#     def jump(dog_name):
#         Dog_dict={item.name : item for item in Dog.instances}
#         print(f'{dog_name} jumps {(Dog_dict[dog_name].height)**2} cm!')

# Dog('Freddy',40)

# davids_dog=Dog('Rex',50)

# print(davids_dog.name, davids_dog.height)

# Dog.jump(davids_dog.name)
# Dog.bark(davids_dog.name)

# sarahs_dog=Dog('Teacup',20)

# print(sarahs_dog.name, sarahs_dog.height)

# Dog.jump(sarahs_dog.name)
# Dog.bark(sarahs_dog.name)

# oldest=Dog.instances[0]

# for item in Dog.instances:
#     if item.height > oldest.height:
#         oldest=item
# print(oldest.name)


# Exercise 3

# class Song:

#     def __init__(self, lyrics:list):
#         self.lyrics = lyrics
#         Song.instances.append(self)

#     def sing_me_a_song(lyrics:list)-> str:
#         for item in lyrics:
#             print(item)
# stairway= Song(["There's a lady who's sure","all that glitters is gold", "and she's buying a stairway to heaven"])

# Song.sing_me_a_song(stairway.lyrics)

# Exercise 4 

# class Zoo:
#     def __init__(self, zoo_name) -> None:
#         self.zoo_name=zoo_name

#     zoo_name=""
#     animals=[]

#     def add_animals(new_animal:str):
#         if new_animal not in Zoo.animals:
#             Zoo.animals.append(new_animal)
#             print('You just added ', new_animal)
#         else:
#             print('That animal is already in the safari! ')
    
#     def get_animals():
#         print(Zoo.animals)

#     def sell_animals(animal_sold):
#         if animal_sold in Zoo.animals:
#             Zoo.animals.remove(animal_sold)
#             print('You just sold ', animal_sold)
#         else:
#             print('That animal is not in this Safari. ')
    
#     def sort_animals(animals)-> list:
#         animals.sort()

#         letters=[]
#         for i,item in enumerate(animals):
#             if i == 0:
#                 letters.append([item])
#             else:
#                 if item[0] == animals[i-1][0]:
#                     letters[-1].append(item)
#                 else:
#                     letters.append([item])
                    
#         return letters

#     def get_groups():
#         print(*Zoo.sort_animals(Zoo.animals), sep='\n')

#     def ramat_gan_safari():

#         Zoo.zoo_name='Ramat Gan Safari'
#         print(f'Welcome to {Zoo.zoo_name}')

#         while True:
#             animal_input=input('Which animal would you like to add to the zoo if finished type "done"? ')
#             if animal_input == 'done':
#                 break
#             else:
#                 Zoo.add_animals(animal_input)

#         print('\nThe animals in the Zoo are...\n')
#         Zoo.get_animals()
#         origin_animals=[item for item in Zoo.animals]
#         while True:
#             user_input=input('''
# To sort the animals type "sort".
# To print the list of original animals type "get1". 
# To print animals in first letter groups type "get2".
# To sell an animal type "sell".
# To add an animal type "add".
# To end program type "end". ''')

#             if user_input == 'sort':
#                 Zoo.animals=Zoo.sort_animals(Zoo.animals)
#                 print('\nList of animals has been sorted.')

#             elif user_input == 'get1':
#                 print('\n',origin_animals)

#             elif user_input == 'get2':
#                 print('\nThe animals in the zoo (A-Z)')
#                 Zoo.get_groups()

#             elif user_input == 'sell':
#                 while True:
#                     sell_input=input('\nWhich animal would you like to sell if finished selling type "done". ')
#                     if sell_input == 'done':
#                         break
#                     else:
#                         Zoo.sell_animals(sell_input)
#             elif user_input == 'add':
#                 while True:
#                     add_input=input('\nWhich animal would you like to add if finished adding type "done". ')
#                     if add_input == 'done':
#                         break
#                     else:
#                         Zoo.add_animals(add_input)
#             elif user_input == 'end':
#                 print("\nThank you for using our program!!")
#                 break
            
#             else:
#                 print("That was not one of the options! Try again.")

# Zoo.ramat_gan_safari()

