import PyPDF2
import re

# K2012 Report of Sale.pdf     starts on page 3

pdfFileObj = open('data/K2012 Report of Sale.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print ( pdfReader.numPages )

page = 2

parcelPattern = re.compile(r'PARCEL NUMBER: ([K0123456789-]*) LEGAL DESCRIPTION: (.+)(\d{2}-\d{3}-\d{2}-\d{2}-\d{2}-\d{1}-\d{2}-\d{3})')

# parcelPattern = re.compile(r'PARCEL NUMBER: ([K0123456789-]*) LEGAL DESCRIPTION: ([\w\d\w\l]+)(\d{2}-\d{3}-\d{2}-\d{2}-\d{2}-\d{1}-\d{2}-\d{3})')

for i in range(2, 10):
    pageObj = pdfReader.getPage(i)

    text =  pageObj.extractText() 

    text =  text.replace(chr(10),' ') 

    # PARCEL NUMBER: K2012-01030

    ret = parcelPattern.search( text ).groups()

    print ( ret )
