import requests

response = requests.get("https://restcountries.com/v3.1/all")
info_dict={}
for i in range(10):
    info_dict.update({response.json()[i]['name']['common']:{'name':response.json()[i]['name']['common'],
    'capital':response.json()[i]['capital'][0],
    'flag':response.json()[i]['flag'],
    'subregion':response.json()[i]['subregion'],
    'population':response.json()[i]['population']}})
print(info_dict.values())


