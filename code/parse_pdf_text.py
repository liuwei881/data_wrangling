#coding=utf-8

pdf_txt = 'data/en-final-table9.txt'
# openfile = open(pdf_txt, 'r')
countries = []
totals = []
double_lined_countries = [
    'Bolivia (Plurinational\n',
    'Democratic People\xe2\x80\x99s\n',
    'Democratic Republic\n',
    'Lao People\xe2\x80\x99s Democratic\n',
    'Micronesia (Federated\n',
    'Saint Vincent and\n',
    'The former Yugoslav\n',
    'United Republic\n',
    'Venezuela (Bolivarian\n',
]


def clean(line):
    """
        清洗代码中的换行符,空格以及其他特殊符号
    """
    line = line.strip('\n').strip()
    line = line.replace('\xe2\x80\x93', '-')
    line = line.replace('\xe2\x80\x99', '\'')
    return line


def turn_on_off(line, status, start, prev_line, end='\n'):
    """
        这个函数用于检查该行是否以特定值开始/结束.
        如果该行确实以特定值开始/结束,则状态设为开/关(真/假)
    """
    if line.startswith(start):
        status = True
    elif status and line == end and prev_line != 'and areas':
        status = False
    return status


with open(pdf_txt, 'r') as openfile:
    country_line = total_line = False
    previous_line = ''
    for line in openfile:
        if country_line:
            if previous_line in double_lined_countries:
                line = ' '.join([clean(previous_line), clean(line)])
                countries.append(clean(line))
            elif line not in double_lined_countries:
                countries.append(clean(line))
        elif total_line:
            if len(line.replace('\n', '').strip()) > 0:
                totals.append(clean(line))
        country_line = turn_on_off(line, country_line,
                                   'and areas', previous_line)
        total_line = turn_on_off(line, total_line,
                                 'total', previous_line)
        previous_line = line


import pprint
data = dict(zip(countries, totals))
pprint.pprint(data)

