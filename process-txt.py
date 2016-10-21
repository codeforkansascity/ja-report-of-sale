import csv
import requests
import json

csv.register_dialect('piper', delimiter='|', quoting=csv.QUOTE_NONE,lineterminator='\n')

myfile = 'K2016Pub.txt'

with open(myfile, newline='') as csvfile:
    for row in csv.DictReader(csvfile, dialect='piper'):
        print (row)
        parcel_number = 'JA' + row['parcel_number'].replace("-", "")
        print (parcel_number)
        url = 'http://dev-api.codeforkc.devel/address-attributes-county-id/V0/' + parcel_number + '?city=Kansas%20City&state=MO'

        myResponse = requests.get(url)
        print (myResponse.status_code)

        # For successful API call, response code will be 200 (OK)
        if(myResponse.ok):

            # Loading the response data into a dict variable
            # json.loads takes in only binary or string variables so using content to fetch binary content
            # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
            jData = json.loads(myResponse.content.decode('utf-8'))
            print("The response contains {0} properties".format(len(jData)))
            print("\n")
            for key in jData['data']:
                if  ( type( key ) is str ):
                    value = jData['data'][key]
                    print ( value )
                        print ('BAD' + key + ' data is ')
                        print ( type( jData['data'][key] ) )
                    else:
                        print (key + " : " + value )
                else:
                    print (key + ' is not a string')
        else:
            # If response code is not ok (200), print the resulting http error code with description
            myResponse.raise_for_status()
