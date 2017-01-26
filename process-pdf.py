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

def strip_data( format, out_file_name, pdf_file_path, pdf_base_name, pdf_start_page, pdf_end_page ):
    pdf_file_name = pdf_file_path + pdf_base_name

    print ( 'Processing ' + pdf_file_name )

    output_csv = open( out_file_name, 'w')
    csv_writer = csv.writer(output_csv, dialect='excel')
    
    # K2012 Report of Sale.pdf     starts on page 3
    
    pdfFileObj = open(pdf_file_name, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    if pdfReader.numPages < pdf_end_page:
        pdf_end_page = pdfReader.numPages

#    parcelPattern = re.compile(r'on (.+), real.+PARCEL NUMBER: ([K0123456789-]*) LEGAL DESCRIPTION: (.+)(\d{2}-.+-.+-.+-.+-.+-.+-.+) judgment and (.+), being the highest.+to the said (.+),\s+at')

    if format == 1:    
        parcelPattern = re.compile(r'on (.+), real.+PARCEL NUMBER: ([K0123456789-]*) LEGAL DESCRIPTION: (.+)(\d{2}-.+-.+-.+-.+-.+-.+-.+) was offered for sale in accordance with and subject to the terms and conditions of the judgment and (.+), being the highest.+to the said (.+),\s+at')
    elif format == 2:
        parcelPattern = re.compile(r'on (.+), real.+PARCEL NUMBER: ([K0123456789-]*).+LEGAL DESCRIPTION:(.+)(\d{2}-.+-.+-.+-.+-.+-.+-.+) was offered for sale in.+judgment and (.+), being the ')
    elif format == 3:
        parcelPattern = re.compile(r'on (.+), real.+PARCEL NUMBER: ([K0123456789-]*).+LEGAL DESCRIPTION:(.+)(\d{2}-.+-.+-.+-.+-.+-.+-.+) was offered')


    parcelPatternB = re.compile(r'on (.+), real.+PARCEL NUMBER: ([K0123456789-]*).+LEGAL DESCRIPTION:(.+)(\d{2}-.+-.+-.+-.+-.+-.+-.+) was offered')
    parcelPatternC = re.compile(r'on (.+), real.+PARCEL NUMBER: ([K0123456789-]*).+LEGAL DESCRIPTION:(.+)was offered')
    parcelPatternD = re.compile(r'on (.+), real.+PARCEL NUMBER: ([K0123456789-]*).+LEGAL DESCRIPTION:(.+)(\d{2}-.+) was offered')

    header = ['Date Sold', 'Parcel Number', 'Legal Description', 'APN', 'Owner Name Address', 'longitude', 'latitude', 'Situs Address','URL', 'Source', 'Page No.']
    
    csv_writer.writerows( [header] )
    
    for i in range(pdf_start_page, pdf_end_page):
        pageObj = pdfReader.getPage(i)
        page_offset = i
    
        text =  pageObj.extractText() 
    
        text =  text.replace(chr(10),' ') 
        text =  text.replace('·','-') 

        ret = parcelPattern.search( text )

        longitude = ''
        latitude = ''
        single_line_address = ''
   
        # For debuging special characters
        #
        # x = ":".join("{:02x}".format(c) for c in bytearray( text, 'utf-8' ) )
        # print ( x ) 
        # print ( text ) 

        isb = 0

        if ret is None:

            ret = parcelPatternB.search( text )
            isb = 1

        if ret is None:

            ret = parcelPatternC.search( text )
            isb = 2

        if ret is None:

            ret = parcelPatternD.search( text )
            isb = 3

        if ret is not None:

            ret = ret.groups()
            ret = list( ret )


            if isb == 1:
                ret.append( '' )
            elif isb == 2:
                ret.append( '' )
                ret.append( '' )
            elif isb == 3:
                ret.append( '' )
            else:
                del ret[5]

            if ret[3] != '':

                api_info = address_api ( ret[3] )

                if api_info is not None:
                    api_info = list( api_info )
                    longitude = api_info[0]
                    latitude = api_info[1]
                    single_line_address = api_info[2]

            ret.append( longitude )
            ret.append( latitude )
            ret.append( single_line_address )

            if ret[3] != '':
                ret.append( 'http://maps.jacksongov.org/PropertyReport/propertyReport.cfm?pid=' + ret[3] )
            else:
                ret.append( '' )

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


#strip_data(1,'K2011-1.csv', 'data/PDFs/2011/','kc report of sale vol. 1-ocr.pdf', 2, 109)
#strip_data(1,'K2011-1-1.csv', 'data/PDFs/2011/','kc report of sale vol. 1-1 ocr.pdf', 0, 999)
#strip_data(1,'K2011-2.csv', 'data/PDFs/2011/','kc report of sale vol. 2 - ocr.pdf', 0, 999)
#strip_data(1,'K2011-2-2.csv', 'data/PDFs/2011/','kc report of sale vol. 2-1- ocr.pdf', 0, 42)

#strip_data(1,'K2012.csv', 'data/PDFs/2012/','OCR_K2013 Report of Sale.pdf', 0, 389)

#strip_data(1,'K2013-1.csv', 'data/PDFs/2013/','KC 1 of 5- ocr.pdf', 0, 999)
#strip_data(1,'K2013-2.csv', 'data/PDFs/2013/','KC 2 of 5 -ocr.pdf', 0, 999)
#strip_data(1,'K2013-3.csv', 'data/PDFs/2013/','KC 3 of 5 - ocr.pdf', 0, 999)
#strip_data(1,'K2013-4.csv', 'data/PDFs/2013/','KC 4of 5- ocr.pdf', 0, 999)
#### NO DATA strip_data(1,'K2013-5.csv', 'data/PDFs/2013/','KC of 5 of 5 and p.4 to 46 LAND TRUST - ocr.pdf', 2, 999)

#strip_data(1,'K2015.csv', 'data/PDFs/2015/','OCR_2015_K-2015 REPORT OF SALE LAND TAX SUIT NO.pdf', 0, 423)
strip_data(1,'OCR_3_K2015.csv', 'data/PDFs/2015/','OCR_3_K-2015 REPORT OF SALE LAND TAX SUIT NO.pdf', 0, 423)

