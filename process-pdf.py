import PyPDF2
import re
import requests
import json
import csv

def cleannone(val):
    if val is None:
        val = '';
    return val

def strip_data( pdf_file_path, pdf_base_name, pdf_start_page, pdf_end_page ):
    pdf_file_name = pdf_file_path + pdf_base_name + '.pdf'

    print ( 'Processing ' + pdf_file_name )

    output_csv = open(pdf_base_name + '.csv', 'w')
    csv_writer = csv.writer(output_csv, dialect='excel')
    
    # K2012 Report of Sale.pdf     starts on page 3
    
    pdfFileObj = open(pdf_file_name, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    if pdfReader.numPages < pdf_end_page:
        pdf_end_page = pdfReader.numPages
    
    
    # parcelPattern = re.compile(r'PARCEL NUMBER: ([K0123456789-]*) LEGAL DESCRIPTION: (.+)(\d{2}-\d{3}-\d{2}-\d{2}-\d{2}-\d{1}-\d{2}-\d{3})')
    amountsPattern = re.compile(r'([\({][0-9\.,\$]+[\)}])')
    
    parcelPattern = re.compile(r'PARCEL NUMBER: ([K0123456789-]*) LEGAL DESCRIPTION: (.+)(\d{2}-\d{3}-\d{2}-\d{2}-\d{2}-\d{1}-\d{2}-\d{3}) .+ judgment and (.+), being the highest.+to the said (.+),\s+at\s+said')
    
    
    header = ['Parcel Number', 'Legal Description', 'APN', 'PDF Name Address', 'PDF Name', 'PDF Address', 'Situs Address', 'URL']
    
    csv_writer.writerows( [header] )
    
    for i in range(pdf_start_page, pdf_end_page):
        pageObj = pdfReader.getPage(i)
    
        text =  pageObj.extractText() 
    
        text =  text.replace(chr(10),' ') 

        ret = parcelPattern.search( text )
    
        if ret is not None:
            ret = ret.groups()
            ret = list( ret )
        
            name_and_address = ret[3]
            name = ret[4]
    
            searchString = name + ', (.+)'
    
            addressPattern = re.compile(searchString)
    
            address = addressPattern.search( name_and_address )
    
            if address is not None:
                address = addressPattern.search( name_and_address ).groups(0)
                ret.append(address[0])
            else:
                ret.append( '' )
    

            single_line_address = address_api ( ret[2] )
            ret.append( single_line_address )

            ret.append( 'http://maps.jacksongov.org/PropertyReport/propertyReport.cfm?pid=' + ret[2] )

            csv_writer.writerows( [ ret ]  )

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


pdf_end_page = 387

strip_data( 'data/', 'K2012 Report of Sale', 2, 387)

#strip_data( 'data/kc report of sale K2011/', 'kc report of sale vol. 1', 2, 10)
#strip_data( 'data/kc report of sale K2011/', 'kc report of sale vol. 1-1', 2, 50)
#strip_data( 'data/kc report of sale K2011/', 'kc report of sale vol. 2', 2, 50)
#strip_data( 'data/kc report of sale K2011/', 'kc report of sale vol. 2-1', 2, 50)

