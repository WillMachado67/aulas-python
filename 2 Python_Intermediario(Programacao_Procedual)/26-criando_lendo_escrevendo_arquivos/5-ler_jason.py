# https://docs.python.org/3/library/functions.html#open
import json

with open('abc.json', 'w+') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)

print(d1_json)
