import csv
import requests
import datetime
from bs4 import BeautifulSoup
import sqlite3
import tempfile

todays_data_url = "http://www.nepalstock.com/todaysprice/export"

requests_nepse_url = requests.get(todays_data_url)

beautifulSoup = BeautifulSoup(requests_nepse_url.content, features="lxml")
dataTable = beautifulSoup.find("table")

output_rows =[]
i = 0
for table_row in dataTable.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text.replace("\n",''))
    output_rows += [output_row]
output_rows.remove([])
print(output_rows)

with open('a.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)