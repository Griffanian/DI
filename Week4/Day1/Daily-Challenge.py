class Farm:

    animals={}
    def __init__(self, name:str):
        self.name = name
        print(f"\n{name}'s farm\n")

    def add_animal(class_name, name:str, num:int=1):

        if name not in list(Farm.animals.keys()):
            Farm.animals.update({name:num})
        else:
            Farm.animals[name]+=num

    def get_info(class_name)->str:
        out_list=[]

        for key,value in Farm.animals.items():
            out_list.append(f"{key} : {value}")

        out_list.append("\n\tE-I-E-I-0!")
        out_str='\n'.join(out_list)

        return out_str
    
    def get_animal_types(class_name)->list:
        return list(Farm.animals)

    def get_short_info(class_name)->str:
        names=macdonald.get_animal_types()
        names[-1]+='s'
        out="McDonald's farm has "+"s, ".join(names)
        return out

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())