another=""
while True:
    num_input=input(f"write {another} a num. ")
    if num_input.isnumeric() == True:
        break
    else:
        another="another"
if int(num_input) % 2 == 0:
    print("number is even")
else:
    print("number is odd")