import requests,random,ExerciseXP

response = requests.get("https://restcountries.com/v3.1/all")
info_dict={}
cols='''name varchar(50),
        capital varchar(50),
        flag varchar(10),
        subregion varchar(50),
        population int'''
ExerciseXP.setup_database('Countries')
ExerciseXP.setup_table('country','countries',cols)

def dict_update(i):
    info_dict.update({response.json()[i]['name']['common']:{'name':response.json()[i]['name']['common'],
        'capital':response.json()[i]['capital'][0],
        'flag':response.json()[i]['flag'],
        'subregion':response.json()[i]['subregion'],
        'population':response.json()[i]['population']}})

for a in range(10):
    num_list=[i for i in range(len(response.json()))]
    while True:
        try:
            i = random.choice(num_list)
            dict_update(i)
            break
        except:
            num_list.remove(i)
            i = random.choice(num_list)
final_query=['''insert into country (name, capital, flag, subregion, population)
values\n''']

for item in info_dict.values():
    query_list=['(']
    for value in item.values():
        try:
            query_list.append(f"{int(value)}, ")
        except ValueError:
            query_list.append(f"'{str(value)}', ")
        
    query_list[-1]=query_list[-1].replace(', ','')
    query_list.append('),\n')
    final_query.append(''.join(query_list))

runnable=''.join(final_query)
runnable=runnable.rstrip(',\n')
print(runnable)
ExerciseXP.run_change_query(runnable,'countries')


