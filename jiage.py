import requests
import csv


f = open('./csv/price.csv',mode='w')
csvw = csv.writer(f)

uri = 'http://www.xinfadi.com.cn/getPriceData.html'


body ={
    "limit":20,
}

for i in range(10):
    body['current'] = i+1
    resp = requests.post(uri,data = body).json()
    
    data = resp['list']
    for i in data:
        name = i['prodName']
        lowPrice = i['lowPrice']
        highPrice = i['highPrice']
        avgPrice = i['avgPrice']
        specInfo = i['specInfo']
        pubDate = i['pubDate']
        csvw.writerow([name,lowPrice,highPrice,avgPrice,specInfo,pubDate])

f.close()

