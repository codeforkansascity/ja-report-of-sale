import PyPDF2
import re
import requests
import json
import csv

pdf_file_path = 'data/'
pdf_base_name = 'K2012 Report of Sale'
pdf_file_name = pdf_file_path + pdf_base_name + '.pdf'

pdf_start_page = 2
pdf_end_page = 387

output_csv = open(pdf_base_name + '.csv', 'w')
csv_writer = csv.writer(output_csv, dialect='excel')

def cleannone(val):
    if val is None:
        val = '';
    return val

# K2012 Report of Sale.pdf     starts on page 3

pdfFileObj = open(pdf_file_name, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

if pdfReader.numPages < pdf_end_page:
    pdf_end_page = pdfReader.numPages


# parcelPattern = re.compile(r'PARCEL NUMBER: ([K0123456789-]*) LEGAL DESCRIPTION: (.+)(\d{2}-\d{3}-\d{2}-\d{2}-\d{2}-\d{1}-\d{2}-\d{3})')
amountsPattern = re.compile(r'([\({][0-9\.,\$]+[\)}])')

parcelPattern = re.compile(r'PARCEL NUMBER: ([K0123456789-]*) LEGAL DESCRIPTION: (.+)(\d{2}-\d{3}-\d{2}-\d{2}-\d{2}-\d{1}-\d{2}-\d{3}) .+ judgment and (.+), being the highest.+to the said (.+),\s+at\s+said')


header = ['Parcel Number', 'Legal Description', 'APN', 'PDF Name Address', 'PDF Name', 'PDF Address']

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

        csv_writer.writerows( [ ret ]  )

