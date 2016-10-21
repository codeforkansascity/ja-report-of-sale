import PyPDF2
import re
import requests
import json
import csv


def cleannone(val):
    if val is None:
        val = '';
    return val

# K2012 Report of Sale.pdf     starts on page 3

pdfFileObj = open('data/K2012 Report of Sale.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print ( pdfReader.numPages )

page = 2

parcelPattern = re.compile(r'PARCEL NUMBER: ([K0123456789-]*) LEGAL DESCRIPTION: (.+)(\d{2}-\d{3}-\d{2}-\d{2}-\d{2}-\d{1}-\d{2}-\d{3})')
amountsPattern = re.compile(r'([\({][0-9\.,\$]+[\)}])')

# judgment and ERMITA PORTALES, 5228 SAIDA AVENUE, KANSAS CITY, MO 64123, being the highest

parcelPattern = re.compile(r'PARCEL NUMBER: ([K0123456789-]*) LEGAL DESCRIPTION: (.+)(\d{2}-\d{3}-\d{2}-\d{2}-\d{2}-\d{1}-\d{2}-\d{3}) .+ judgment and (.+), being the highest.+to the said (.+),\s+at\s+said')

output_csv = open('K2012 Report of Sale.csv', 'w')

csv_writer = csv.writer(output_csv, dialect='excel')

header = {'Parcel Number', 'Legal Description', 'APN', 'PDF Name Address', 'PDF Name', 'PDF Address'}


csv_writer.writerows( [header] )

for i in range(2, 387):
    pageObj = pdfReader.getPage(i)

    text =  pageObj.extractText() 

    text =  text.replace(chr(10),' ') 

#    print ( text )

    # PARCEL NUMBER: K2012-01030

    ret = parcelPattern.search( text ).groups()
    print ( ret) 
#    amts = amountsPattern.search( text ).groups()

#    print ( amts )

    
    name_and_address = ret[3]
    name = ret[4]


    searchString = name + ', (.+)'

    addressPattern = re.compile(searchString)

    address = addressPattern.search( name_and_address ).groups(0)

    print ( '|' + address[0] + '|' )

    ret = list( ret )

    ret.append(address[0])

    # print ( ret )

    # ['K2012-01048', 'SECTION 35 TWNSHP 50 RANGE 33 BEG 501 FT N OF NE COR OF ST JOHN AVE & DENVER AVE, THS 33 FT, TH E 135 FT, TH N 33 FT, TH W TO BEG ', '13-810-25-05-00-0-00-000', 'RIGHTEOUS PROPERTIES, LLC, 6324 N CHATHAM AVE, #327 KANSAS CITY, MO 64151', 'RIGHTEOUS PROPERTIES, LLC', ('6324 N CHATHAM AVE, #327 KANSAS CITY, MO 64151',)]

    data = {'Parcel Number': ret[0], 'Legal Description': ret[1], 'APN': ret[2], 'PDF Name Address': ret[3], 'PDF Name': ret[4], 'PDF Address': ret[5] }
    csv_writer.writerows( [ ret ]  )

    parcel_number = 'JA' + ret[2].replace("-", "")

    # http://dev-api.codeforkc.org//address-attributes/V0/10001%20N%20CHERRY%20DR%2C?city=Kansas%20City&state=mojj

    url = 'http://dev-api.codeforkc.org/address-attributes-county-id/V0/' + parcel_number + '?city=Kansas%20City&state=MO'

    myResponse = requests.get(url)
    # print (myResponse.status_code)

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
        print("The response contains {0} properties".format(len(jData)))
        # print( jData )

        address_api_data = jData['data']
        
        single_line_address = cleannone(address_api_data['single_line_address'])
        county_situs_address = cleannone(address_api_data['county_situs_address'])
        longitude = address_api_data['longitude']
        latitude = address_api_data['latitude']

    

#        for key in jData['data']:
#            if  ( str is None):
#                print (key + ' is not a string')
#            else:
#                value = jData['data'][key]
#                print ( type( jData['data'][key] ) )
#                print (key + ' = ' + value)
    else:
        # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()

    data['single_line_address'] = single_line_address
    data['county_situs_address'] = county_situs_address
    data['longitude'] = longitude
    data['latitude'] = latitude

    
    # print ( data )
    
    print ( ' ' )
    print ( ret[2] )
    print ( ret[5] )
    print ( single_line_address )
    print ( county_situs_address )
    print ( ' ' )



