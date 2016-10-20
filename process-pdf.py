import PyPDF2
import re
import requests

# K2012 Report of Sale.pdf     starts on page 3

pdfFileObj = open('data/K2012 Report of Sale.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print ( pdfReader.numPages )

page = 2

parcelPattern = re.compile(r'PARCEL NUMBER: ([K0123456789-]*) LEGAL DESCRIPTION: (.+)(\d{2}-\d{3}-\d{2}-\d{2}-\d{2}-\d{1}-\d{2}-\d{3})')
amountsPattern = re.compile(r'([\({][0-9\.,\$]+[\)}])')

# judgment and ERMITA PORTALES, 5228 SAIDA AVENUE, KANSAS CITY, MO 64123, being the highest

parcelPattern = re.compile(r'PARCEL NUMBER: ([K0123456789-]*) LEGAL DESCRIPTION: (.+)(\d{2}-\d{3}-\d{2}-\d{2}-\d{2}-\d{1}-\d{2}-\d{3}) .+ judgment and (.+), being the highest.+to the said (.+),\s+at\s+said')



for i in range(2, 10):
    pageObj = pdfReader.getPage(i)

    text =  pageObj.extractText() 

    text =  text.replace(chr(10),' ') 

    print ( text )

    # PARCEL NUMBER: K2012-01030

    ret = parcelPattern.search( text ).groups()

#    amts = amountsPattern.search( text ).groups()

    print ( amts )

    
    name_and_address = ret[3]
    name = ret[4]

    searchString = name + ', (.+)'

    addressPattern = re.compile(searchString)

    address = addressPattern.search( name_and_address ).groups(0)

    print ( '|' + address[0] + '|' )

    ret = list( ret )

    ret.append(address)

    print ( ret )

    # ['K2012-01048', 'SECTION 35 TWNSHP 50 RANGE 33 BEG 501 FT N OF NE COR OF ST JOHN AVE & DENVER AVE, THS 33 FT, TH E 135 FT, TH N 33 FT, TH W TO BEG ', '13-810-25-05-00-0-00-000', 'RIGHTEOUS PROPERTIES, LLC, 6324 N CHATHAM AVE, #327 KANSAS CITY, MO 64151', 'RIGHTEOUS PROPERTIES, LLC', ('6324 N CHATHAM AVE, #327 KANSAS CITY, MO 64151',)]

    data = {'Parcel Number': ret[0], 'Legal Description': ret[1], 'APN': ret[2], 'PDF Name Address': ret[3], 'PDF Name': ret[4], 'PDF Address': ret[5] }



    print ( data )

