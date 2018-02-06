#coding=utf-8

import re

word = '\w+'    # 1
sentence = 'Here is my sentence.'

print re.findall(word, sentence)  # 2
search_result = re.search(word, sentence)   # 3
print search_result.group(0)   # 4
match_result = re.match(word, sentence) # 5
print match_result.group(0)