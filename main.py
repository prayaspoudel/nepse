import requests
from bs4 import BeautifulSoup

company_list_link = "http://www.nepalstock.com/company/index/1/?stock-name=&stock-symbol=&sector-id=&_limit=500"

company_get_request = requests.get(company_list_link)

companyListSoup = company_get_request.content
