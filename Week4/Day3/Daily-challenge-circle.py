import turtle,string,math
from random import *
class Circle:
    instances={}
    def __init__(self,name:str,radius:int):
        self.name=name
        self.radius=radius
        self.diameter=radius*2
        self.area=math.pi*((radius)**2)
        Circle.instances.update({self.name:self})
        if self.radius!=0:
            print(f'the circles area is {self.area}')
            self.draw_circle()
    
    @classmethod
    def from_diameter(cls,name,diameter:int):
        new_circle=cls(name,diameter/2)
        return new_circle
    
    def listed_circles():
        list_circles=[item.radius for item in list(Circle.instances.values())]
        return list_circles
    
    def sort_listed_circles(item=listed_circles()):
        item.sort()
        print("list of circles has been sorted")
        return item
    
    def draw_circle(self):
        t = turtle.Turtle()
        t.circle(self.radius)

    def __add__(self,other):
        adder_radius=self.radius+other.radius
        new_circle=Circle(f'Added circle of {self.name} and {other.name}',adder_radius) 
        return new_circle

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius
         
    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False
        
    def rand_str(length:int):
        string1=''.join([choice(string.ascii_uppercase) for _ in range(length)])
        return(string1)
        

miles=Circle.from_diameter("Miles",100)
freddy=Circle("Freddy",30)

print(Circle.sort_listed_circles())


turtle.exitonclick()

