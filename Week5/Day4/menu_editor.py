from ExerciseXP import *

def load_manager(name,price):
    item=MenuItem(name,price)
    return item
def show_user_menu(name='Resturant'):
    setup_database()
    setup_table()   
    for item in MenuItem.all():
        load_manager(item[0],item[1])
    while True:
        user_input=input("""
Menu
(a) Add an item
(d) Delete an item
(v) View the menu
(x) Exit 
Please choose an option. """)
        if user_input == 'a':
            add_item_to_menu()
        elif user_input == 'd':
            remove_item_from_menu()
        elif user_input == 'v':
            show_restaurant_menu()
        elif user_input == 'x':
            break
        else:
            print("That was not one of the options")
            
def add_item_to_menu():
    name=input("Please enter the name of item you wish to add. ")
    price=input("Please enter the price of item you wish to add. ")
    item=load_manager(name,price)
    item.save()
    if (name,price) in MenuItem.all():
        print("item was added successfully.")

def remove_item_from_menu():
    name=input("Please enter the name of the item you wish to remove ")
    try:
        MenuItem.delete(MenuItem.instances[name])
    except KeyError:
        print(MenuItem.instances)
    if name in [item[0] for item in MenuItem.all()]:
        print("item was not deleted successfully")
    else:
        print("item was deleted successfully")
def show_restaurant_menu():
    print(MenuItem.all())

show_user_menu()