import csv
import requests
import json

csv.register_dialect('piper', delimiter='|', quoting=csv.QUOTE_NONE,lineterminator='\n')

output_csv = open('new.csv', 'w')
csv_writer = csv.writer(output_csv, dialect='excel')


def cleannone(val):
    if val is None:
        val = '';
    return val

def address_api( p ):

    parcel_number = 'JA' + p.replace("-", "")

    # http://dev-api.codeforkc.org//address-attributes/V0/10001%20N%20CHERRY%20DR%2C?city=Kansas%20City&state=mojj

    url = 'http://dev-api.codeforkc.org/address-attributes-county-id/V0/' + parcel_number + '?city=Kansas%20City&state=MO'

    myResponse = requests.get(url)

    single_line_address = ''
    county_situs_address = ''
    longitude = ''
    latitude = ''

    # For successful API call, response code will be 200 (OK)
    if(myResponse.ok):

        # Loading the response data into a dict variable
        # json.loads takes in only binary or string variables so using content to fetch binary content
        # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)

        jData = json.loads(myResponse.content.decode('utf-8'))

        address_api_data = jData['data']
        
        single_line_address = cleannone(address_api_data['single_line_address'])
        county_situs_address = cleannone(address_api_data['county_situs_address'])
        longitude = address_api_data['longitude']
        latitude = address_api_data['latitude']

        return single_line_address

myfile = 'K2016Pub.txt'



with open(myfile, newline='') as csvfile:
    for row in csv.DictReader(csvfile, dialect='piper'):
        print (row)
        single_line_address = address_api ( row['parcel_number']  )

        row = list( row )
        row.append( single_line_address )

        csv_writer.writerows( [ row ]  )
