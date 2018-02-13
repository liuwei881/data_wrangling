#coding=utf-8


import json



country_codes = json.loads(open('data/iso-2.json', 'rb').read())
country_dict = {}

for c in country_codes:
    country_dict[c.get('name')] = c.get('alpha-2')


def get_country_code(row):
    return country_dict.get(row['Countries and areas'])


ranked = ranked.compute([('country_code',
                          agate.Formula(text_type, get_country_code)),
                         ])
for r in ranked.where(lambda x: x.get('country_code') is None).rows:
    print r['Countries and areas']


import pygal

worldmap_chart = pygal.maps.world.World()
worldmap_chart.title = 'Child Labor Worldwide'

cl_dict = {}
for r in ranked.rows:
    cl_dict[r.get('country_code_complete').lower()] = r.get('Total (%)')

worldmap_chart.add('Total Child Labor (%)', cl_dict)
worldmap_chart.render()