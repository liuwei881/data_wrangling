#coding=utf-8

from csv import reader

data_rdr = reader(open('data/mn.csv', 'rb'))
header_rdr = reader(open('data/mn_headers_updated.csv', 'rb'))

data_rows = [d for d in data_rdr]
header_rows = [h for h in header_rdr if h[0] in data_rows[0]]   # 1

# print len(header_rows)

all_short_headers = [h[0] for h in header_rows]
skip_index = [] # 2
final_header_rows = []

for header in data_rows[0]:
    if header not in all_short_headers:
        index = data_rows[0].index(header)  # 3
        skip_index.append(index)
    else:
        for head in header_rows:
            if head[0] == header:
                final_header_rows.append(head)
                break

new_data = []

for row in data_rows[1:]:   # 4
    new_row = []
    for i, d in enumerate(row): # 5
        if i not in skip_index: # 6
            new_row.append(d)
    new_data.append(new_row)    # 7

zipped_data = []

for drow in new_data:
    zipped_data.append(zip(final_header_rows, drow))

# for x in zipped_data[0]:
#     print 'Question: {}\nAnswer: {}'.format(x[0][1], x[1])

# for x in enumerate(zipped_data[0][:20]):
#     print x

from datetime import datetime

start_string = '{}/{}/{} {}:{}'.format(
    zipped_data[0][8][1], zipped_data[0][7][1], zipped_data[0][9][1],
    zipped_data[0][13][1], zipped_data[0][14][1]
)

start_time = datetime.strptime(start_string, '%m/%d/%Y %H:%M')
# print start_time

# for answer in zipped_data[0]:
#     if not False:
#         print answer


datatypes = {}  # 1

start_dict = {
    'digit': 0, 'boolean': 0,
    'empty': 0, 'time_related': 0,
    'text': 0, 'unknown': 0
}   # 2

for row in zipped_data:
    for resp in row:
        question = resp[0][1]
        answer = resp[1]
        key = 'unknown' # 3
        if answer.isdigit():    # 4
            key = 'digit'
        elif answer in ['Yes', 'No', 'True', 'False']:  # 5
            key = 'boolean'
        elif answer.isspace():  # 6
            key = 'empty'
        elif answer.find('/') > 0 or answer.find(':') > 0:  # 7
            key = 'time_related'
        elif answer.isalpha():  # 8
            key = 'text'
        if question not in datatypes.keys():    # 9
            datatypes[question] = start_dict.copy() # 10
        datatypes[question][key] += 1   # 11
print datatypes
