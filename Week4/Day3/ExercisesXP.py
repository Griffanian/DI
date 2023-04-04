# Exercise 1

# class Ops:
    
#     def __init__(self,name,value=0) -> None:
#         self.name=name
#         self.value=value
#     def __str__(self) -> str:
#         return self.name
#     def __abs__(self):
#         '''changes the value to absoloute form'''
#         if self.value <0:
#             self.value=-self.value
#         return self
#     def __int__(self)->int:
#         '''changes value to iteger form'''
#         self.value=int(self.value)
#         return self.value
#     def __input__(self):
#         '''stores a user input in object'''
#         input1=input(self.name)
#         self.input_str=input1
#         return self
    
    
    
# one=Ops('one','1')
# two=Ops('what')

# Exercise 2

class Currency:
    instances={}
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
        Currency.instances.update({len(Currency.instances):self})
    
    def __str__(self) -> str:
        return f'{self.amount} {self.currency}'
    
    def __int__(self) -> None:
        return self.amount

    def __repr__(self) -> str:
        return f'{self.amount} {self.currency}'
    
    def __add__(self,other):
        if other in Currency.instances.values():
            if self.currency == other.currency:
                return self.amount + other.amount
            else:
                raise TypeError(f"Cannot add between Currency type {self.currency} and {other.currency}")
        elif type(other)==int:
            return self.amount + other
        else:
            raise ValueError
    def __iadd__(self,other):
        if other in Currency.instances.values():
            if self.currency == other.currency:
                return self
            else:
                raise TypeError(f"Cannot add between Currency type {self.currency} and {other.currency}")
        elif type(other)==int:
            self.amount+=other
            return self
        else:
            raise ValueError
    

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
c1+=2
print(c1+c3)