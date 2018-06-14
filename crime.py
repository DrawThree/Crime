import urllib.request as req
import json

def read_crime_data_from_url():
    url = 'https://data.austintexas.gov/resource/qxhx-pr9e.json?go_location_zip=78705'
    fin = req.urlopen(url)
    data = fin.read()
    return data.decode('utf8')

def deserialize_crime_data(crimes):
    deserialized_crimes = json.loads(crimes)
    return deserialized_crimes

def make_warwick_list(crimes):
    warwick_crimes = []
    for crime in crimes:
        try:
            if crime['go_location'].find('WEST') >= 0:
                warwick_crimes.append(crime)
        except KeyError:
            continue
    return warwick_crimes

def write_warwick_list(warwick_crimes):    
    with open('warwick.txt', mode='w', encoding='utf8') as fout:
        json_string = json.dumps(warwick_crimes)
        fout.write(json_string)
        
'''    
with open('crime.txt', encoding='utf8') as fin:
    data = fin.read()
'''
crimes = read_crime_data_from_url()
deserialized_crimes = deserialize_crime_data(crimes)
warwick_crimes = make_warwick_list(deserialized_crimes)

for crime in warwick_crimes:
	print(crime['go_report_date'] + ', ' +
              crime['go_location'].strip() + ', ' +
              crime['go_highest_offense_desc'])
