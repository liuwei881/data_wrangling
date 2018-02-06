#coding=utf-8

from fuzzywuzzy import fuzz, process


# my_records = [
#     {
#         'favorite_food': 'cheesecake',
#         'favorite_drink': 'wine, beer, and tequila',
#         'favorite_dessert': 'cheese or cake',
#     },
#     {
#         'favorite_food': 'cheese',
#         'favorite_drink': 'beer, wine, and tequila',
#         'favorite_dessert': 'cheese cake',
#     }]

# print fuzz.ratio(my_records[0].get('favorite_book'),
#                  my_records[1].get('favorite_book'))
#
# print fuzz.ratio(my_records[0].get('favorite_movie'),
#                  my_records[1].get('favorite_movie'))
#
# print fuzz.ratio(my_records[0].get('favorite_show'),
#                  my_records[1].get('favorite_show'))
#
#
# print fuzz.partial_ratio(my_records[0].get('favorite_book'),
#                          my_records[1].get('favorite_book'))
#
# print fuzz.partial_ratio(my_records[0].get('favorite_movie'),
#                          my_records[1].get('favorite_movie'))
#
# print fuzz.partial_ratio(my_records[0].get('favorite_show'),
#                          my_records[1].get('favorite_show'))

# print fuzz.ratio(my_records[0].get('favorite_food'),
#                             my_records[1].get('favorite_food'))
#
# print fuzz.token_set_ratio(my_records[0].get('favorite_drink'),
#                             my_records[1].get('favorite_drink'))
#
# print fuzz.token_set_ratio(my_records[0].get('favorite_dessert'),
#                             my_records[1].get('favorite_dessert'))

choices = ['Yes', 'No', 'Maybe', 'N/A']
print process.extract('ya', choices, limit=2)
print process.extractOne('ya', choices)
print process.extract('nope', choices, limit=2)
print process.extractOne('nope', choices)