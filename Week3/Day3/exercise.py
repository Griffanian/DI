# Exercise 1

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# print(dict(zip(keys,values)))

# Exercise 2

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# price=0
# for value in family:
#     if value < 3:
#         pass
#     elif value < 12:
#         price+=10
#     else:
#         price+=15

# Exercise 3

# brand_dict={"name": "Zara", 'creation_date': 1975, 'creator_name': 'Amancio Ortega Gaona', 'type_of_clothes': ["men", "women", "children", 'home'], 'international_competitors': ['Gap', 'H&M', 'Benetton'], 'number_stores': 7000 , 'major_color':{ 'France': 'blue', 'Spain': 'red',
#     'US': ['pink', "green"]}}

# brand_dict['number_stores']=2

# print("Zara's clients are men, women, and children who are interested in fashion and home decor.")

# brand_dict.update({"country_creation":"Spain"})
# print(brand_dict)

# if 'international_competitors' in list(brand_dict.keys()):
#     brand_dict['international_competitors'].append('Desigual.')

# del brand_dict['creation_date']

# print(brand_dict['international_competitors'][-1])

# print(brand_dict['major_color']['US'])

# print(len(brand_dict))

# print(list(brand_dict.keys()))

# more_on_zara={
#     'creation_date': 1975, 
#     'number_stores': 10000
# }

# brand_dict.update({'creation_date':more_on_zara['creation_date']})
# brand_dict.update({'number_stores':more_on_zara['number_stores']})
# print(brand_dict['number_stores'])

# Exercise 4

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# disney_users_A={key:i for i, key in enumerate(users)}

# print(disney_users_A)

# disney_users_B=dict(enumerate(users))

# print(disney_users_B)

# users.sort()
# disney_users_C={key:i for i, key in enumerate(users)}
# print(disney_users_C)

disney_users_C={i:value for i, value in enumerate(users) if ('i' in value) or (list(value)[0]=='P') or (value[0]=="M") }
print(disney_users_C)