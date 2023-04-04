# Exercise 2
from random import *
import string,datetime,math


def compare(num:int)->str:
    comp_num=randint(0,100)
    if comp_num == num:
        print("Success")
    else:
        print('Fail')
def rand_str(length:int):
    string1=''.join([choice(string.ascii_uppercase) for _ in range(length)])
    print(string1)

# def time_now(): 
#     now1 = datetime.datetime.now()  
#     return(now1)

# def time_till_new():
#     times_list=time_till()
#     print(f"the first of Jan is in {times_list[1]} weeks {times_list[2]} days and {times_list[3]}:{times_list[4]}:{times_list[5]}")

# def time_till(date:list=[2024,1,1]):
#     date1= datetime.datetime(*date)
#     now1 = datetime.datetime.now()  
#     till = date1 - now1
#     return secs_times(till.total_seconds())

# def secs_times(secs:int):
#     total=abs(round(secs,0))

#     years=math.floor(total/31557600)
#     total-=years*31557600

#     weeks=math.floor(total/604800)
#     total-=weeks*604800

#     days=math.floor(total/86400)
#     total-=days*86400

#     hours=math.floor(total/3600)
#     total-=hours*3600

#     minutes=math.floor(total/60)
#     total-=minutes*60

#     seconds=math.floor(total)
#     return [years, weeks, days, hours, minutes ,seconds]

# def time_alive(date:list=[2004,5,13]):
#     timing_list=time_till(date)
#     print(f"You have been alive {timing_list[0]*525600+timing_list[1]*10080+timing_list[2]*1440+timing_list[3]} minutes")

# def time_till_holiday(date=[2023,4,6]):
#     times_list=time_till(date)
#     print(f"the next holiday is in {times_list[1]} weeks {times_list[2]} days and {times_list[3]}:{times_list[4]}:{times_list[5]}")

# def planatery_age(planet,age_in_secs:int=1000000000)->str:
#     time=[]
#     earth_yrs=(age_in_secs/31557600)
#     time+=[earth_yrs/0.2408467,earth_yrs/0.61519726,earth_yrs,earth_yrs/ 11.862615, earth_yrs/29.447498, earth_yrs/ 84.016846, earth_yrs/ 164.79132]
#     return time[planet-1]

# Exercise 9

# people=[]

# from faker import Faker
# for i in range(3):
#     fake=Faker()
#     people.append({'name':fake.name(),'address':fake.address(),'code':fake.language_code()})
    
# print(people)