import requests
import tempfile
from bs4 import BeautifulSoup
import csv
import datetime
import schedule
import time

def mainFunction():
    floor_sheet_link = "http://www.nepalstock.com/floorsheet?_limit=50000"

    floor_sheet_request = requests.get(floor_sheet_link)

    beautifulSoup = BeautifulSoup(floor_sheet_request.content, features="lxml")
    dataTable = beautifulSoup.find("table")

    output_rows =[]
    for table_row in dataTable.findAll('tr')[2:-3]:
        columns = table_row.findAll('td')
        output_row = []
        for column in columns:
            output_row.append(column.text.replace("\n",'').strip())
        output_rows += [output_row]
    try:
        output_rows.remove([])
    except:
        pass

    with open(str(datetime.datetime.now())[:10].replace('-','')+'_floorsheet.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(output_rows)

schedule.every().day.at("07:25").do(mainFunction)

while True:
    schedule.run_pending()
    time.sleep(1)