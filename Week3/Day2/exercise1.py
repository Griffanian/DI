# Exercise 1
#  my_fav_numbers ={2,7,13}
# numbers_list=list(my_fav_numbers)
# numbers_list.append(5)
# numbers_list.append(9)
# numbers_list.sort()
# numbers_list.pop()
# my_fav_numbers=set(numbers_list)
# friend_fav_numbers={3,5,13,19}
# our_fav_numbers=my_fav_numbers | friend_fav_numbers

# Exercise 2

# No

# Exercise 3

# basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# basket.remove("Banana")
# basket.pop()
# basket.append("Kiwi")
# basket.insert(0, "Apples")
# basket.count("Apples")
# basket.clear()
# print(basket)

# Exercise 4

# integer is a whole number. Float is a decimal.

# floats1=[]
# for i in range (10):
#     floats2.append(i/2 + 1)
    
# Exercise 5 

# for i in range(20):
#     print(i+1)
# list1=['a', 's', 'd', 'f', 'g', 'h', 'j', 'g', 't', 's', 'd', 'f', 'g', 'v', 'b', 'n', 'h', 'g', 'f', 'd', 's', 'f', 'g', 'b', 'n', 'h', 'g', 'f', 'd', 's', 'f', 'g', 'h''f', 'g', 'v', 'b', 'n', 'h', 'g', 'f', 'd', 's', 'f', 'g', 'b', 'n', 'h', 'g', 'f', 'd', 's', 'f', 'g', 'h']
# for i in range(1,20):
#     if i%2==0:
#         print(list1[i])

# Exercise 6

# name_input=""

# while name_input != "Miles":
#     name_input=input("what is your name? ")

# Exercise 7

# fruits_input=input("what are your favorite fruits (eg. apple mango cherry.)? ")
# fruit_list =fruits_input.split()
# print(fruit_list)
# fruits_input2=input("Give me fruit ")
# if fruits_input2 in fruit_list:
#     print ("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy")

# Exercise 8

# user_list=[]

# while True:
#     user_input=input("Give me a pizza topping or type quit if you are finished. ")
#     if user_input == "quit":
#         break
#     user_list.append(user_input)
#     print(f"You added {user_input} to your pizza!")
# topping= " ".join(user_list)
# price=10+(len(user_list))*2.5
# print(f"Your pizza will have {topping} on it and it will cost {price}")

# Exercise 9

# guest_input=int(input("how many guests are there? "))
# price=0

# for i in range (guest_input):
#     age_input=int(input("how old is the next guest? "))
#     if age_input < 3:
#         pass
#     elif age_input < 12:
#         price+=10
#     else:
#         price+=15

# print(f"your total is {price}")

# names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Hannah", "Isaac", "Jack"]
# names1=[]

# for i in range(len(names)-1):
#     age_input=int(input(f"{names[i]} what is your age? "))
#     if 16 < age_input < 21:
#         names1.append(names[i])
# print(names1)


# Exercise 10

# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
# finished_samwiches=[]

# for x in range(len(sandwich_orders)):
#     finished_samwiches.append(sandwich_orders[x])
#     print(f"I made your {sandwich_orders[x]}")

# Exercise 11

sandwich_orders = ["Pastrami sandwich", "Tuna sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_samwiches=[]

print("The deli is out of pastrami")

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

for x in range(len(sandwich_orders)):
    finished_samwiches.append(sandwich_orders[x])
    print(f"I made your {sandwich_orders[x]}")


