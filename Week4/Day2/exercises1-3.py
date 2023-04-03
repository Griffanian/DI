from exercises import Dog
from random import randint

class PetDog(Dog):
    def __init__(self, name: str, age: int, weight: int, trained:bool=False) -> None:
        super().__init__(name, age, weight)
        self.trained=trained
    
    def train(self):
        print(self.bark())
        self.trained=True

    def play(*args):
        print(f"{' '.join([item.name for item in args])} all play together")
    def do_a_trick(self):
        if self.trained == True:
            tricks = [f'{self.name} does a barrel roll',f'{self.name} stands on his back legs',f'{self.name} shakes your had',f'{self.name} plays dead']
            random_int=randint(0,3)
            print(tricks[random_int])
        else:
            print('Dog must be trained to do tricks.')

dog1=PetDog("dog1",10,50)
dog2=PetDog("dog2",8,60)
dog3=PetDog("dog3",12,40)

dog1.train()

dog1.do_a_trick()