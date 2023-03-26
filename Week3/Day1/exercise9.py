height_input = input("what is your height in inches (eg. 5 10)")
height_list=list(height_input)
if len(height_list)<=3:
    height_feet = (float(height_list[0]) + float(height_list[2])/12)
else:
    height_feet= int(height_list[0]) + (((int(height_list[2])*10)+int(height_list[3]))/12)
height_cm = height_feet * 30.48
print(f"{height_cm} cm")
if height_cm > 145:
    print("you are tall enough to ride")
else:
    print("you are not tall enough to ride")