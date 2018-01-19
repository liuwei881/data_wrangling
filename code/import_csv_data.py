#coding=utf-8

import csv


with open('data/data-text.csv', 'rt', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)