#coding=utf-8

import agate
import xlrd

cpi_workbook = xlrd.open_workbook('data/corruption_perception_index.xls')
cpi_sheet = cpi_workbook.sheets()[0]


for r in range(cpi_sheet.nrows):
    print r, cpi_sheet.row_values(r)


cpi_title_rows = zip(cpi_sheet.row_values(1), cpi_sheet.row_values(2))
cpi_titles = [' '.join([t[0], t[1]]) for t in cpi_title_rows]
cpi_titles = [t.strip() for t in cpi_titles]

cpi_rows = [cpi_sheet.row_values(r) for r in range(3, cpi_sheet.nrows)]
cpi_types = get_types(cpi_sheet.row(3))


def get_types(example_row):
    types = []
    for v in example_row:
        value_type = ctype_text[v.ctype]
        if value_type == 'text':
            types.append(text_type)
        elif value_type == 'number':
            types.append(number_type)
        elif value_type == 'xldate':
            types.append(date_type)
        else:
            types.append(text_type)
    return types


def get_table(new_arr, types, titles):
    try:
        table = agate.Table(new_arr, titles, types)
        return table
    except Exception as e:
        print e


import json

country_json = json.loads(open('data/earth.json', 'rb').read())
country_dict = {}

for dct in country_json:
    country_dict[dct['name']] = dct['parent']


def get_country(country_row):
    return country_dict.get(country_row['Country / Territory'].lower())


cpi_and_cl = cpi_and_cl.compute([('continent',
                                  agate.Formula(text_type, get_country)),
                                 ])


for r in cpi_and_cl.rows:
    print r['Country / Teeritory'], r['continent']


no_continent = cpi_and_cl.where(lambda x: x['continent'] is None)

for r in no_continent.rows:
    print r['Country / Territory']


africa_cpi_cl = cpi_and_cl.where(lambda x: x['continent'] == 'africa')
for r in africa_cpi_cl.order_by('Total (%)', reverse=True).rows:
    print "{}: {}% - {}".format(r['Country / Territory'], r['Total (%)'],
                                r['CPI 2013 Score'])


import numpy

print numpy.corrcoef(
    [float(t) for t in africa_cpi_cl.columns['Total (%)'].values()],
    [float(c) for c in africa_cpi_cl.columns['CPI 2013 Score'].values()])[0, 1]

africa_cpi_cl = africa_cpi_cl.compute([('Africa Child Labor Rank',
                                        agate.Rank('Total (%)', reverse=True)),
                                       ])
africa_cpi_cl = africa_cpi_cl.compute([('Africa CPI Rank',
                                        agate.Rank('CPI 2013 Score')),
                                       ])


cl_mean = africa_cpi_cl.aggregate(agate.Mean('Total (%)'))
cpi_mean = africa_cpi_cl.aggregate(agate.Mean('CPI 2013 Score'))


def highest_rates(row):
    if row['Total (%)'] > cl_mean and row['CPI 2013 Score'] < cpi_mean:
        return True
    return False


highest_cpi_cl = africa_cpi_cl.where(lambda x: highest_rates(x))

for r in highest_cpi_cl.rows:
    print "{}: {}% - {}".format(r['Country / Territory'], r['Total (%)'],
                                r['CPI 2013 Score'])