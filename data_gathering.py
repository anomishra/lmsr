from bs4 import BeautifulSoup
import requests
import csv

rows = []
for year in ['2014', '2015', '2016']:
    for month in range(1,13):
        try:
            print ('{}, {}'.format(year, month))
            url = 'https://iemweb.biz.uiowa.edu/pricehistory/PriceHistory_GetData.cfm?Market_ID=360&Month={:02d}&Year={}'.format(month, year)
            print(url)
            html = requests.get(url)
            soup = BeautifulSoup(html.text, 'lxml')
            table = soup.select_one("table")
            row = [[td.text.replace(' ', '').replace('\xa0\xa0\xa0\xa0', '') for td in row.find_all("td")] for row in table.select("tr + tr")]

            rows = rows + row
            print(rows)
        except Exception as e:
            pass

header=['Date', 'Contract', 'Units' ,'Volume', 'LowPrice', 'HighPrice', 'AvgPrice', 'LastPrice']
with open("data_collected.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow(header)
    wr.writerows(rows)
