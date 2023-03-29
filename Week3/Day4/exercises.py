from random import randint,uniform

def display_message() -> str:
    print("I am learning to code")
display_message()

def favourite_book(title:str) -> str:
    print(f"One of my favorite books is {title}")
favourite_book("Alice in wonderland")

def describe_city(city:str, country="Iceland") -> str:
    print(f"{city} is in {country}")
describe_city("reykjavik")

def rand_compare(num1:int) -> str:
    num2=randint(0,100)
    if num1==num2:
        print("Great succes")
    else:
        print(f"Failure number was {num2}")

def make_shirt(size="Large", text="I love python") -> str:
    print(f'the size of the shirt is {size} and the text is "{text}"')

make_shirt()
make_shirt("Medium")
make_shirt("Small", "done!")
make_shirt(text="done")

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians()->str:
    print(*magician_names, sep="\n")
show_magicians()
def make_great()->str:
    magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
    magician_names=[item+" the Great" for item in magician_names]
    print(*magician_names, sep="\n")
make_great()

def get_random_temp(season='') -> int:
    if season == "winter":
        return uniform(-10,16)
    elif season == "spring":
        return uniform (3,25)
    elif season == "summer":
        return uniform (20,40)
    elif season == "autumn":
        return uniform (16,30)
    else:
        return NameError("that not a real season")

def main(season='') -> str:
    temp=get_random_temp(season)
    print(f"the temperature right now is {temp}")
    try:
        if temp < 0:
            print("Brrr, that's freezing! Wear some extra layers today")
        elif 0 < temp < 16:
            print("Quite chilly! Don't forget your coat")
        elif 16 < temp < 23:
            print("not too cold") 
        elif 24 < temp < 32:
            print("Wow great weather enjoy")
        elif 32 < temp < 40:
            print("Make sure to wear sunscreen")
        else:
            print("get_random_temp is broken")
    except TypeError:
        print("Please include a season as an argument eg.'summer' ")
main("winter")
