import requests
# from lxml import etree
import json
import csv

from concurrent.futures import ThreadPoolExecutor


f = open('csv/xinfadi.csv',mode='w',encoding='utf-8')
csvwrite = csv.writer(f)

def download_page(uri,num):
    body={
                'limit': 20,
                "current": num
            }
    resp = requests.post(uri,data = body)
    html = resp.json()
    # print(html)
    for i in html["list"]:
        prodName = i['prodName']
        lowPrice = i['lowPrice']
        highPrice = i['highPrice']
        avgPrice = i['avgPrice']
        place = i['place']
        unitInfo = i['unitInfo']
        pubDate = i['pubDate'].split(" ")[0]

        csvwrite.writerow([prodName,lowPrice,highPrice,avgPrice,place,unitInfo,pubDate])
    print(uri,f"{num}写入完成")




if __name__ == "__main__":

    with ThreadPoolExecutor(50) as t:
        for i in range(1,200):
            
            t.submit(download_page('http://www.xinfadi.com.cn/getPriceData.html',i))