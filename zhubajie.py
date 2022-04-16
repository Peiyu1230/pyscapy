import requests
from lxml import etree
import csv

f = open("./csv/shop.csv",mode='w')
csvw = csv.writer(f)


uri = 'https://beijing.zbj.com/search/f/?kw=saas'

resp = requests.get(uri)
# print(resp.text)
html = etree.HTML(resp.text)
alls = html.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div')
for i in alls:
    shop = i.xpath('./div/div/a[1]/div/p/text()')[1].strip()
    local = i.xpath('./div/div/a[1]/div/div/span/text()')[0]
    price = i.xpath('./div/div/a[2]/div/div/span/text()')[0]
    # text = "saas".join(i.xpath('./div/a[2]/div/div/p/text()')[0])
    text = i.xpath('./div/div/a[2]/div/div/p/text()')
    text = 'saas'.join(text)

    csvw.writerow([shop,text,local,price])


print("over")
f.close()