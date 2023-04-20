import json
with open('/Users/Miles/DI/Week5/Day5/ExerciseXP/mysite/polls/static/animals.json', 'r') as f:
        data = json.load(f)
print(data['animals'][1])
