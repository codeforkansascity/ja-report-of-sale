#! python3

import re
import binascii
import requests
import csv
import requests
import json

def cleannone(val):
    if val is None:
        val = '';
    return val

addressPattern = re.compile(r'<span style="padding-left:10px;">(.+)</span>')

def get_ja_address(url):
    res = requests.get( url )
    address = '';
    if ( res.status_code == requests.codes.ok ):
       text = res.text
       ret = addressPattern.search( text )
       if ret is None:
          address = ''
       else:
          ret = ret.groups()
          ret = list( ret )
          address = ret[0]

    return address

def format_apn(v):
    val = '-'.join([v[2:4],v[4:7],v[7:9],v[9:11],v[11:13],v[13:14],v[14:16],v[16:19]])
    return val

def address_api( p ):

    parcel_number = 'JA' + p.replace("-", "")

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

#        print ( address_api_data )

        single_line_address = cleannone(address_api_data['street_address'])
        longitude = cleannone(address_api_data['longitude'])
        latitude = cleannone(address_api_data['latitude'])
        apn = format_apn(cleannone(address_api_data['county_id']))

        return longitude, latitude, single_line_address, apn


csv.register_dialect('piper', delimiter='|', quoting=csv.QUOTE_NONE,lineterminator='\n')

def update_apn(infile, outfile):

    output_csv = open(outfile, 'w')
    csv_writer = csv.writer(output_csv)

    with open(infile, newline='') as csvfile:
        for row in csv.DictReader(csvfile):

#            row = list( row )

            print ( row['APN'])

            single_line_address = ''
            longitude = ''
            latitude = ''
            neighborhood = ''
            kiva_pin = ''
            kiva_url = ''
            apn = ''

            api_info = address_api ( row[ 'APN' ]  )

            if api_info is not None:
                if  api_info:
                    api_info = list( api_info )
                    apn = api_info[3]
                    kiva_url = 'http://maps.jacksongov.org/PropertyReport/propertyReport.cfm?pid=' + apn
                    county_address = get_ja_address( kiva_url )

                    address = api_info[2]
                    if ( address.upper() == county_address ):
                        longitude = api_info[0]
                        latitude = api_info[1]
                        single_line_address = api_info[2]
                    else:
                        print ( address + ' <> ' + county_address )
                        single_line_address = 'ERROR ' + address + ' <> ' + county_address

#            if api_info is not None:
#                api_info = list( api_info )
#                longitude = api_info[0]
#                latitude = api_info[1]
#                single_line_address = api_info[2]
#                print ( single_line_address )


            rec = []
            rec.append ( row[ 'Date Sold' ] )
            rec.append ( row[ 'Parcel Number' ] )
            rec.append ( row[ 'Legal Description' ] )
            rec.append ( row[ 'APN' ] )
            rec.append ( row[ 'Owner Name Address' ] )

            rec.append( longitude )
            rec.append( latitude )
            rec.append( single_line_address )

            rec.append ( row[ 'URL' ] )
            rec.append ( row[ 'Source' ] )
            rec.append ( row[ 'Page No.' ] )


            csv_writer.writerows( [ rec ]  )

#update_apn('apn-added/K2011-1-1.csv','K2011-1-1.csv')
#update_apn('apn-added/K2011-1.csv','K2011-1.csv')
#update_apn('apn-added/K2011-2-2.csv','K2011-2-2.csv')
#update_apn('apn-added/K2011-2.csv','K2011-2.csv')
#update_apn('apn-added/K2012.csv','K2012.csv')
#update_apn('apn-added/K2013-1.csv','K2013-1.csv')
#update_apn('apn-added/K2013-2.csv','K2013-2.csv')
#update_apn('apn-added/K2013-3.csv','K2013-3.csv')
#update_apn('apn-added/K2013-4.csv','K2013-4.csv')
update_apn('apn-added/K2015.csv','K2015.csv')

