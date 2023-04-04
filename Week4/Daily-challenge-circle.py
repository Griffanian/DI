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
    def listed_circles():
        list_circles=[(value.radius)for value in Circle.instances.values()]
        return list_circles
    def sort_listed_circles(item):
        item.sort()
        print("list of circles has been sorted")
        return item
    def draw_circle(self):
        inst_keys=list(Circle.instances.keys())
        num=inst_keys.index(self.name)
        t = turtle.Turtle()
        # if num > 0:
        #     t.penup()
        #     t.goto((Circle.instances[inst_keys[num-1]].diameter+10),0)
        #     t.pendown()
        t.circle(self.radius)

    def __add__(self,other):
        adder_radius=self.radius+other.radius
        Circle('',adder_radius) 

    def __gt__(self, other):
        if self.radius > other.radius:
            return True
        else:
            return False
    def __lt__(self, other):
        if self.radius < other.radius:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False
    def rand_str(length:int):
        string1=''.join([choice(string.ascii_uppercase) for _ in range(length)])
        return(string1)
        

miles=Circle("Miles",10)
freddy=Circle("Freddy",30)

print(Circle.sort_listed_circles(Circle.listed_circles()))


turtle.exitonclick()

