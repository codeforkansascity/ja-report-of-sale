# Notes
* Python3

# 17-Feb-2017

At the bottom of both of these programs are the files they processed 

## process-pdf.py Used to convert OCRed PDFs into CSV, was initialy going to be the only conversion.
  * Goes out to address API using the APN to retriev longitude, latitude, and single_line_addressj

## process-txt.py Used to update corrected CSV files
  * Goes out to address API using the APN to retriev longitude, latitude, and single_line_addressj
  * Goes out to Jackson County site to verify address that Address API returns, makes not in righthand column.

## Directories

* OUTPUT: K-v2, K-v3, To-Legal-Aid-2016-01-25, apn-added, apn-added-2 
* Input: data/PDFs,  
* Original pdfs to the best of my knowledge `org-data`


Other notes on PDF conversion


R2014 is the same files as R2013.

In j2015 there are some OCR_1_ through OCR_3_, they are conversions using Acrobat three options to convert.  They were not as good as the coversion that Brian had provided.

* 2011 - Michael R
* 2012 - Did not need to OCR
*  2013 - Brian
* 2014 - Same as 2013
* 2015 - Brian


Files with Date and Time

````
-rw-r--r--@  1 paulb  staff  8734149 Jan 27 09:52 Court Administrator's Report of Sale  K 2014 - ocr.pdf
drwxr-xr-x  27 paulb  staff      918 Feb  1 07:46 K-v2
-rw-r--r--   1 paulb  staff   142318 Jan 29 21:28 K-v2.gz
drwxr-xr-x   6 paulb  staff      204 Feb 12 14:40 K-v3
-rw-r--r--   1 paulb  staff      393 Oct 22 00:36 K2016Pub.txt
-rw-r--r--   1 paulb  staff     1077 Oct 17 17:59 LICENSE
-rw-r--r--   1 paulb  staff     6703 Jan 26 22:03 OCR_3_K2015.csv
-rw-r--r--   1 paulb  staff      887 Feb 17 19:17 README.md
drwxr-xr-x  12 paulb  staff      408 Jan 26 01:02 To-Legal-Aid-2016-01-25
-rw-r--r--   1 paulb  staff   104655 Jan 26 01:04 To-Legal-Aid-2016-01-25.zip
drwxr-xr-x  13 paulb  staff      442 Feb 12 14:35 apn-added
drwxr-xr-x   5 paulb  staff      170 Feb 11 19:49 apn-added-2
-rw-r--r--   1 paulb  staff      126 Jan 26 23:11 d
drwxr-xr-x   9 paulb  staff      306 Jan 25 21:31 data
drwxr-xr-x  10 paulb  staff      340 Jan 26 13:27 org-data
-rw-r--r--   1 paulb  staff     6742 Jan 27 09:58 process-pdf.py
-rw-r--r--   1 paulb  staff     5336 Feb 12 14:39 process-txt.py
-rw-r--r--   1 paulb  staff    20166 Jan 27 00:19 test.csv
-rw-r--r--@  1 paulb  staff  8734149 Jan 27 09:53 test.pdf

./K-v2:
total 3032
-rw-r--r--  1 paulb  staff   22060 Jan 28 16:19 K2011-1-1_v2.csv
-rw-r--r--@ 1 paulb  staff   34304 Feb  1 07:46 K2011-1-1_v2.xls
-rw-r--r--  1 paulb  staff    6498 Jan 26 22:03 K2011-1.csv
-rw-r--r--@ 1 paulb  staff   13824 Feb  1 07:45 K2011-1.xls
-rw-r--r--  1 paulb  staff   35571 Jan 28 16:50 K2011-1_v2.csv
-rw-r--r--@ 1 paulb  staff   50688 Feb  1 07:46 K2011-1_v2.xls
-rw-r--r--  1 paulb  staff   14388 Jan 28 17:02 K2011-2-2_v2.csv
-rw-r--r--@ 1 paulb  staff   23552 Feb  1 07:45 K2011-2-2_v2.xls
-rw-r--r--  1 paulb  staff   34565 Jan 28 17:31 K2011-2_v2.csv
-rw-r--r--@ 1 paulb  staff   49152 Feb  1 07:45 K2011-2_v2.xls
-rw-r--r--  1 paulb  staff  131932 Jan 28 18:59 K2012_v2.csv
-rw-r--r--@ 1 paulb  staff  165888 Feb  1 07:45 K2012_v2.xls
-rw-r--r--  1 paulb  staff   30354 Jan 28 19:27 K2013-1_v2.csv
-rw-r--r--@ 1 paulb  staff   45568 Feb  1 07:44 K2013-1_v2.xls
-rw-r--r--  1 paulb  staff   31697 Jan 28 19:55 K2013-2_v2.csv
-rw-r--r--@ 1 paulb  staff   46592 Feb  1 07:44 K2013-2_v2.xls
-rw-r--r--  1 paulb  staff   30715 Jan 28 20:22 K2013-3_v2.csv
-rw-r--r--@ 1 paulb  staff   46080 Feb  1 07:44 K2013-3_v2.xls
-rw-r--r--  1 paulb  staff   30188 Jan 28 20:53 K2013-4_v2.csv
-rw-r--r--@ 1 paulb  staff   45568 Feb  1 07:44 K2013-4_v2.xls
-rw-r--r--  1 paulb  staff  161554 Jan 29 19:43 K2014_v2.csv
-rw-r--r--@ 1 paulb  staff  188416 Feb  1 07:43 K2014_v2.xls
-rw-r--r--  1 paulb  staff  114646 Jan 28 22:40 K2015_v2.csv
-rw-r--r--@ 1 paulb  staff  148992 Feb  1 07:43 K2015_v2.xls

./K-v3:
total 1224
-rw-r--r--  1 paulb  staff  161580 Feb 11 23:25 K2014_v3.csv
-rw-r--r--@ 1 paulb  staff  188928 Feb 12 14:38 K2014_v3.xls
-rw-r--r--  1 paulb  staff  115033 Feb 11 20:47 K2015_v3.csv
-rw-r--r--@ 1 paulb  staff  150016 Feb 12 14:37 K2015_v3.xls

./To-Legal-Aid-2016-01-25:
total 1008
-rw-r--r--  1 paulb  staff   24095 Jan 26 00:25 K2011-1-1.csv
-rw-r--r--  1 paulb  staff   38395 Jan 26 00:24 K2011-1.csv
-rw-r--r--  1 paulb  staff   15339 Jan 26 00:25 K2011-2-2.csv
-rw-r--r--  1 paulb  staff   37120 Jan 26 00:25 K2011-2.csv
-rw-r--r--  1 paulb  staff  142469 Jan 26 00:26 K2012.csv
-rw-r--r--  1 paulb  staff   32104 Jan 26 00:26 K2013-1.csv
-rw-r--r--  1 paulb  staff   33610 Jan 26 00:27 K2013-2.csv
-rw-r--r--  1 paulb  staff   31969 Jan 26 00:27 K2013-3.csv
-rw-r--r--  1 paulb  staff   30844 Jan 26 00:27 K2013-4.csv
-rw-r--r--  1 paulb  staff  110832 Jan 26 00:28 K2015.csv

./apn-added:
total 1320
-rw-r--r--@ 1 paulb  staff   23253 Jan 26 23:01 K2011-1-1.csv
-rw-r--r--@ 1 paulb  staff   37336 Jan 26 23:01 K2011-1.csv
-rw-r--r--@ 1 paulb  staff   14869 Jan 26 23:01 K2011-2-2.csv
-rw-r--r--@ 1 paulb  staff   35940 Jan 26 23:01 K2011-2.csv
-rw-r--r--@ 1 paulb  staff  137974 Jan 26 23:01 K2012.csv
-rw-r--r--@ 1 paulb  staff   31383 Jan 26 23:01 K2013-1.csv
-rw-r--r--@ 1 paulb  staff   32843 Jan 26 23:01 K2013-2.csv
-rw-r--r--@ 1 paulb  staff   31389 Jan 26 23:01 K2013-3.csv
-rw-r--r--@ 1 paulb  staff   30253 Jan 26 23:01 K2013-4.csv
-rw-r--r--@ 1 paulb  staff  168311 Jan 27 10:25 K2014.csv
-rw-r--r--@ 1 paulb  staff  109668 Jan 26 23:53 K2015.csv

./apn-added-2:
total 936
-rw-r--r--  1 paulb  staff  161009 Feb 11 19:48 K2014_v2.csv
-rw-r--r--@ 1 paulb  staff  204288 Feb 11 19:39 K2014_v2.xls
-rw-r--r--@ 1 paulb  staff  110032 Feb 11 19:39 K2015.csv

./data:
total 12080
-rw-r--r--@ 1 paulb  staff    76207 Oct 12 16:50 I 2016 Pub.txt
-rwxr-xr-x@ 1 paulb  staff  3044606 Oct  5 14:47 K2012 Report of Sale.pdf
-rw-r--r--@ 1 paulb  staff  2827963 Oct 13 09:16 K2012 Report of Sale.zip
-rw-r--r--@ 1 paulb  staff   226513 Oct 12 16:50 K2016Pub.txt
drwxr-xr-x@ 9 paulb  staff      306 Jan 27 09:56 PDFs
drwx------@ 6 paulb  staff      204 Oct 17 17:53 kc report of sale K2011

./data/PDFs:
total 0
drwxr-xr-x  11 paulb  staff  374 Jan 25 22:03 2011
drwxr-xr-x   5 paulb  staff  170 Jan 25 21:21 2012
drwxr-xr-x   8 paulb  staff  272 Jan 25 22:11 2013
drwxr-xr-x   9 paulb  staff  306 Jan 27 09:56 2014
drwxr-xr-x   7 paulb  staff  238 Jan 26 01:00 2015
drwxr-xr-x  19 paulb  staff  646 Jan 25 21:42 old-2013

./data/PDFs/2011:
total 35296
-rw-r--r--@ 1 paulb  staff   770995 Jan 25 22:01 kc report of sale vol. 1-1 ocr.pdf
-rwxr-xr-x@ 1 paulb  staff  2068031 Jan 25 21:08 kc report of sale vol. 1-1.pdf
-rw-r--r--@ 1 paulb  staff  1271699 Jan 25 15:55 kc report of sale vol. 1-ocr.pdf
-rwxr-xr-x@ 1 paulb  staff  3064337 Jan 25 21:08 kc report of sale vol. 1.pdf
-rw-r--r--@ 1 paulb  staff  1176676 Jan 25 16:03 kc report of sale vol. 2 - ocr.pdf
-rw-r--r--@ 1 paulb  staff  1905025 Jan 25 16:03 kc report of sale vol. 2-1- ocr.pdf
-rwxr-xr-x@ 1 paulb  staff  4895043 Jan 25 21:08 kc report of sale vol. 2-1.pdf
-rwxr-xr-x@ 1 paulb  staff  2899922 Jan 25 21:08 kc report of sale vol. 2.pdf

./data/PDFs/2012:
total 22176
-rwxr-xr-x@ 1 paulb  staff  3044606 Jan 25 21:08 K2013 Report of Sale.pdf
-rw-r--r--@ 1 paulb  staff  8305283 Jan 25 21:08 OCR_K2013 Report of Sale.pdf

./data/PDFs/2013:
total 11416
-rw-r--r--@ 1 paulb  staff  1183333 Jan 25 22:08 KC 1 of 5- ocr.pdf
-rw-r--r--@ 1 paulb  staff  1174412 Jan 25 22:08 KC 2 of 5 -ocr.pdf
-rw-r--r--@ 1 paulb  staff  1169399 Jan 25 22:08 KC 3 of 5 - ocr.pdf
-rw-r--r--@ 1 paulb  staff  1179512 Jan 25 22:08 KC 4of 5- ocr.pdf
-rw-r--r--@ 1 paulb  staff  1133700 Jan 25 22:08 KC of 5 of 5 and p.4 to 46 LAND TRUST - ocr.pdf

./data/PDFs/2014:
total 67712
-rw-r--r--@ 1 paulb  staff   8734149 Jan 27 09:55 Court Administrator's Report of Sale  K 2014 - ocr.pdf
-rwxr-xr-x@ 1 paulb  staff  11332741 Sep 25  2015 Court Administrator's Report of Sale  K 2014.pdf
-rw-r--r--@ 1 paulb  staff   3747885 Jan 26 22:15 OCR-97-K2014.doc
-rw-r--r--@ 1 paulb  staff   3099681 Jan 26 21:47 OCR-Court Administrators Report of Sale  K 2014.pdf
-rw-r--r--@ 1 paulb  staff   1130839 Jan 26 22:07 OCR-K2014.docx
-rw-r--r--@ 1 paulb  staff   3099735 Jan 26 22:04 OCR-K2014.pdf
-rw-r--r--@ 1 paulb  staff   3509775 Jan 26 22:18 OCR-T-K2014.pdf

./data/PDFs/2015:
total 60256
-rwxr-xr-x@ 1 paulb  staff   2120433 Jan 25 21:08 K-2015 REPORT OF SALE LAND TAX SUIT NO.pdf
-rw-r--r--@ 1 paulb  staff   5008740 Jan 26 00:37 OCR_1_K-2015 REPORT OF SALE LAND TAX SUIT NO.pdf
-rw-r--r--@ 1 paulb  staff   5341980 Jan 25 21:08 OCR_2015_K-2015 REPORT OF SALE LAND TAX SUIT NO.pdf
-rw-r--r--@ 1 paulb  staff   2944908 Jan 26 00:47 OCR_2_K-2015 REPORT OF SALE LAND TAX SUIT NO.pdf
-rw-r--r--@ 1 paulb  staff  15428455 Jan 26 01:00 OCR_3_K-2015 REPORT OF SALE LAND TAX SUIT NO.pdf

./data/PDFs/old-2013:
total 42216
-rwxr-xr-x@ 1 paulb  staff  1448747 Jan 25 21:08 KC 1 of 5.pdf
-rwxr-xr-x@ 1 paulb  staff  1435806 Jan 25 21:08 KC 2 of 5.pdf
-rwxr-xr-x  1 paulb  staff  1426404 Jan 25 21:08 KC 3 of 5.pdf
-rwxr-xr-x@ 1 paulb  staff  1441624 Jan 25 21:08 KC 4of 5.pdf
-rwxr-xr-x@ 1 paulb  staff  1514358 Jan 25 21:08 KC of 5 of 5 and p.4 to 46 LAND TRUST copy.pdf
-rwxr-xr-x@ 1 paulb  staff  1514358 Jan 25 21:08 KC of 5 of 5 and p.4 to 46 LAND TRUST.pdf
-rw-r--r--@ 1 paulb  staff  1183350 Jan 25 21:08 OCR_2013_KC 1 of 5.pdf
-rw-r--r--@ 1 paulb  staff  1173560 Jan 25 21:08 OCR_2013_KC 2 of 5.pdf
-rw-r--r--@ 1 paulb  staff  1169410 Jan 25 21:08 OCR_2013_KC 3 of 5.pdf
-rw-r--r--@ 1 paulb  staff  1178670 Jan 25 21:08 OCR_2013_KC 4of 5.pdf
-rw-r--r--@ 1 paulb  staff  1133704 Jan 25 21:08 OCR_2013_KC of 5 of 5 and p.4 to 46 LAND TRUST copy.pdf
-rw-r--r--  1 paulb  staff  1133702 Jan 25 21:08 OCR_2013_KC of 5 of 5 and p.4 to 46 LAND TRUST.PDF
-rw-r--r--@ 1 paulb  staff  1183346 Jan 25 21:08 OCR_KC 1 of 5.pdf
-rw-r--r--@ 1 paulb  staff  1173558 Jan 25 21:08 OCR_KC 2 of 5.pdf
-rw-r--r--  1 paulb  staff  1169404 Jan 25 21:08 OCR_KC 3 of 5.pdf
-rw-r--r--  1 paulb  staff  1178664 Jan 25 21:08 OCR_KC 4of 5.pdf
-rw-r--r--@ 1 paulb  staff  1133706 Jan 25 21:08 OCR_KC of 5 of 5 and p.4 to 46 LAND TRUST.PDF

./data/kc report of sale K2011:
total 25264
-rwxr-xr-x@ 1 paulb  staff  2068031 Nov 28  2012 kc report of sale vol. 1-1.pdf
-rwxr-xr-x@ 1 paulb  staff  3064337 Nov 28  2012 kc report of sale vol. 1.pdf
-rwxr-xr-x@ 1 paulb  staff  4895043 Nov 28  2012 kc report of sale vol. 2-1.pdf
-rwxr-xr-x@ 1 paulb  staff  2899922 Nov 28  2012 kc report of sale vol. 2.pdf

./org-data:
total 85424
drwxr-xr-x@ 4 paulb  staff       136 Jan 26 13:26 2014
-rw-r--r--@ 1 paulb  staff   2827963 Jan 25 21:38 K2012 Report of Sale (2).zip
-rwxr-xr-x@ 1 paulb  staff   3044606 Oct  5 15:47 K2012 Report of Sale.pdf
drwxr-xr-x@ 8 paulb  staff       272 Jan 26 13:27 PDFs
-rw-r--r--@ 1 paulb  staff  28117543 Jan 25 21:37 PDFs.zip
drwx------@ 6 paulb  staff       204 Jan 25 21:38 kc report of sale K2011 (1)
-rw-r--r--@ 1 paulb  staff   9740201 Jan 25 21:37 kc report of sale K2011 (1).zip

./org-data/2014:
total 21104
-rw-r--r--@ 1 paulb  staff  10802718 Jan 26 13:22 Court Administrator's Report of Sale  K 2014.zip

./org-data/PDFs:
total 0
drwxr-xr-x@ 6 paulb  staff  204 Oct  7 16:51 2011
drwxr-xr-x@ 3 paulb  staff  102 Oct  7 16:51 2012
drwxr-xr-x@ 7 paulb  staff  238 Oct  7 16:51 2013
drwxr-xr-x  7 paulb  staff  238 Jan 26 13:26 2014-BAD
drwxr-xr-x@ 3 paulb  staff  102 Oct  7 16:51 2015

./org-data/PDFs/2011:
total 25264
-rwxr-xr-x@ 1 paulb  staff  2068031 Oct  7 16:51 kc report of sale vol. 1-1.pdf
-rwxr-xr-x@ 1 paulb  staff  3064337 Oct  7 16:51 kc report of sale vol. 1.pdf
-rwxr-xr-x@ 1 paulb  staff  4895043 Oct  7 16:51 kc report of sale vol. 2-1.pdf
-rwxr-xr-x@ 1 paulb  staff  2899922 Oct  7 16:51 kc report of sale vol. 2.pdf

./org-data/PDFs/2012:
total 5952
-rwxr-xr-x@ 1 paulb  staff  3044606 Oct  7 16:51 K2012 Report of Sale.pdf

./org-data/PDFs/2013:
total 14208
-rwxr-xr-x@ 1 paulb  staff  1448747 Oct  7 16:51 KC 1 of 5.pdf
-rwxr-xr-x@ 1 paulb  staff  1435806 Oct  7 16:51 KC 2 of 5.pdf
-rwxr-xr-x@ 1 paulb  staff  1426404 Oct  7 16:51 KC 3 of 5.pdf
-rwxr-xr-x@ 1 paulb  staff  1441624 Oct  7 16:51 KC 4of 5.pdf
-rwxr-xr-x@ 1 paulb  staff  1514358 Oct  7 16:51 KC of 5 of 5 and p.4 to 46 LAND TRUST.pdf

./org-data/PDFs/2014-BAD:
total 14208
-rwxr-xr-x@ 1 paulb  staff  1448747 Oct  7 16:51 KC 1 of 5.pdf
-rwxr-xr-x@ 1 paulb  staff  1435806 Oct  7 16:51 KC 2 of 5.pdf
-rwxr-xr-x@ 1 paulb  staff  1426404 Oct  7 16:51 KC 3 of 5.pdf
-rwxr-xr-x@ 1 paulb  staff  1441624 Oct  7 16:51 KC 4of 5.pdf
-rwxr-xr-x@ 1 paulb  staff  1514358 Oct  7 16:51 KC of 5 of 5 and p.4 to 46 LAND TRUST.pdf

./org-data/PDFs/2015:
total 4144
-rwxr-xr-x@ 1 paulb  staff  2120433 Oct  7 16:51 K-2015 REPORT OF SALE LAND TAX SUIT NO.pdf

./org-data/kc report of sale K2011 (1):
total 25264
-rwxr-xr-x@ 1 paulb  staff  2068031 Nov 28  2012 kc report of sale vol. 1-1.pdf
-rwxr-xr-x@ 1 paulb  staff  3064337 Nov 28  2012 kc report of sale vol. 1.pdf
-rwxr-xr-x@ 1 paulb  staff  4895043 Nov 28  2012 kc report of sale vol. 2-1.pdf
-rwxr-xr-x@ 1 paulb  staff  2899922 Nov 28  2012 kc report of sale vol. 2.pdf
````


# 26-Jan-2017

R2014 is the same files as R2013.

In j2015 there are some OCR_1_ through OCR_3_, they are conversions using Acrobat three options to convert.  They were not as good as the coversion that Brian had provided.

2011 - Michael R
2012 - Did not need to OCR
2013 - Brian
2014 - Same as 2013
2015 - Brian


