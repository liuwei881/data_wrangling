#coding=utf-8

import dataset

db = dataset.connect('sqlite:///data/data_wrangling.db')

table = db['unicef_survey']

for row_num, data in enumerate(zipped_data):
    for question, answer in data:
        data_dict = {
            'question': question[1],
            'question_code': question[0],
            'answer': answer,
            'response_number': row_num,
            'survey': 'mn',
            }
        table.insert(data_dict)


from csv import writer


def write_file(zipped_data, file_name):
    with open(file_name, 'wb') as new_csv_file:
        wrtr = writer(new_csv_file)
        titles = [row[0][1] for row in zipped_data[0]]
        wrtr.writerow(titles)
        for row in zipped_data:
            answers = [resp[1] for resp in row]
            wrtr.writerow(answers)


write_file(zipped_data, 'cleaned_unicef_data.csv')