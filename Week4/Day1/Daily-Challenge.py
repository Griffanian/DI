class Farm:
    def __init__(self, name:str):
        self.name = name
        self.animals={}
        print(f"\n{self.name}'s farm\n")

    def add_animal(self, animal:str, num:int=1):

        if animal in self.animals:
            self.animals[animal]+=num
        else:
            self.animals[animal]= num

    def get_info(self)->str:
    
        out_list=[f"{animal} : {num}" for animal,num in macdonald.animals.items()]
        out_list.append("\n\tE-I-E-I-0!")
        out_str='\n'.join(out_list)
        return out_str
    
    def get_animal_types(self)->list:
        return list(macdonald.animals)

    def get_short_info(self)->str:
        names=macdonald.get_animal_types() 

        names_list=[items+'s 'for items in names if items !=names[-1]]
        names_list.append(f'and {names[-1]}s')
        names_list.insert(0,f"{self.name}'s farm has")
        out_str=' '.join(names_list)
        
        return out_str

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())