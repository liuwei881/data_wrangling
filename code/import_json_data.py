#coding=utf-8

import json


with open('data/data-text.json', 'r', encoding='utf-8') as jsonfile:
    data = json.loads(jsonfile.read())
    for row in data:
        print(row)