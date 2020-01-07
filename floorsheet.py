import requests
import tempfile
from bs4 import BeautifulSoup
import csv
import datetime

todays_data_link = "http://www.nepalstock.com/floorsheet?_limit=50000"

company_get_request = requests.get(todays_data_link)

companyListSoup = company_get_request.content

#temp = tempfile.TemporaryFile()

beautifulSoup = BeautifulSoup(company_get_request.content, features="lxml")
dataTable = beautifulSoup.find("table")

output_rows =[]
i = 0
for table_row in dataTable.findAll('tr')[2:-3]:
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text.encode('utf-8').replace("\n",'').strip())
    output_rows += [output_row]
try:
    output_rows.remove([])
except:
    pass
#print(output_rows)

with open(str(datetime.datetime.now())[:10].replace('-','')+'_floorsheet.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)