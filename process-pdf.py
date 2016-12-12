import PyPDF2
import re
import requests
import json
import csv
import binascii

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

#    parcelPattern = re.compile(r'on (.+), real.+PARCEL NUMBER: ([K0123456789-]*) LEGAL DESCRIPTION: (.+)(\d{2}-.+-.+-.+-.+-.+-.+-.+) judgment and (.+), being the highest.+to the said (.+),\s+at')
    
    parcelPattern = re.compile(r'on (.+), real.+PARCEL NUMBER: ([K0123456789-]*) LEGAL DESCRIPTION: (.+)(\d{2}-.+-.+-.+-.+-.+-.+-.+) was offered for sale in accordance with and subject to the terms and conditions of the judgment and (.+), being the highest.+to the said (.+),\s+at')

    header = ['Date Sold', 'Parcel Number', 'Legal Description', 'APN', 'Owner Name Address', 'longitude', 'latitude', 'Situs Address','URL', 'Source', 'Page No.']
    
    csv_writer.writerows( [header] )
    
    for i in range(pdf_start_page, pdf_end_page):
        pageObj = pdfReader.getPage(i)
        page_offset = i
    
        text =  pageObj.extractText() 
    
        text =  text.replace(chr(10),' ') 

        ret = parcelPattern.search( text )

        longitude = ''
        latitude = ''
        single_line_address = ''
   
        # For debuging special characters
        #
        # x = ":".join("{:02x}".format(c) for c in bytearray( text, 'utf-8' ) )
        # print ( x ) 
        # print ( text ) 


        if ret is not None:
            ret = ret.groups()
            ret = list( ret )
        
            del ret[5]

            api_info = address_api ( ret[2] )

            if api_info is not None:
                api_info = list( api_info )
                longitude = api_info[0]
                latitude = api_info[1]
                single_line_address = api_info[2]

            ret.append( longitude )
            ret.append( latitude )
            ret.append( single_line_address )

            ret.append( 'http://maps.jacksongov.org/PropertyReport/propertyReport.cfm?pid=' + ret[2] )

            ret.append( pdf_file_name )

            ret.append( page_offset + 1 )

            csv_writer.writerows( [ ret ]  )
        else:
            error_msg = 'Could not process page ' + str(page_offset + 1) 
            print ( error_msg )

            ret = [ error_msg ]
            csv_writer.writerows( [ ret ]  )

    print ( 'Last page processed ')

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
        
        single_line_address = cleannone(address_api_data['single_line_address']) + ' ' + cleannone(address_api_data['zip'])
        longitude = cleannone(address_api_data['longitude'])
        latitude = cleannone(address_api_data['latitude'])

        return longitude, latitude, single_line_address


pdf_end_page = 108

#strip_data( 'data/', 'K2012 Report of Sale', 2, pdf_end_page )

#strip_data( './', 'OCR_kc report of sale vol. 1', 2, pdf_end_page )
strip_data( 'data/PDFs/2014/', 'OCR_2014_KC 2 of 5', 0, 99 )


# The following were not text
#strip_data( 'data/kc report of sale K2011/', 'kc report of sale vol. 1', 2, 10)
#strip_data( 'data/kc report of sale K2011/', 'kc report of sale vol. 1-1', 2, 50)
#strip_data( 'data/kc report of sale K2011/', 'kc report of sale vol. 2', 2, 50)
#strip_data( 'data/kc report of sale K2011/', 'kc report of sale vol. 2-1', 2, 50)

