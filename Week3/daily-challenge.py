import random
another="a"
while True:
    str_input=input(f"give me {another} 10 charecter string ")
    if len(str_input) < 10:
        print("string is too short")
        another="another"
    elif len(str_input) > 10:
        print("string is too long")
        another="another"
    else:
        break
str_list = list(str_input)
print(str_list[0],str_list[len(str_list)-1])
str_list2=[]

for i in range(len(str_list)):
    (str_list2.append(str_list[i]))
    print(''.join(str_list2))
random.shuffle(str_list)
print(''.join(str_list))