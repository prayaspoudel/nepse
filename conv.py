import csv
import requests
import datetime
from bs4 import BeautifulSoup
import sqlite3
import tempfile

nepse_url = "http://www.nepalstock.com/todaysprice/export"

database = "database.db"

sqlDB = sqlite3.connect(database)

#company_table_query = " CREATE TABLE"

requests_nepse_url = requests.get(nepse_url)
dump_file_name = str(datetime.datetime.now())[:10].replace('-','')
data_dump_from_url = open(dump_file_name + ".htm", 'wb')
data_dump_from_url.write(requests_nepse_url.content)

beautifulSoup = BeautifulSoup(requests_nepse_url.content, features="lxml")
dataTable = beautifulSoup.find("table")

output_rows =[]
i = 0
for table_row in dataTable.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    #output_row.remove([''])
    output_rows += [output_row]
output_rows.remove([])
print(output_rows)

with open(dump_file_name + '.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)