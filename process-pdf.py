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

        csv_writer.writerows( [ ret ]  )

