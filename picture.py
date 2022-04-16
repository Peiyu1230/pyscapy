# 使用bs4 爬取图片


import requests
from bs4 import BeautifulSoup as bp
import time

domian = 'https://www.umeitu.com'

def get_page(url):

    uri = domian + url

    resp = requests.get(uri,verify = False)
    resp.encoding='utf-8'

    main1 = bp(resp.text,"html.parser")
    return main1

main_page = get_page('/bizhitupian/meinvbizhi/yangyanmeinv.htm')

alist = main_page.find("div",class_="TypeList").find_all("a")

alist_all = []
for i in alist:
    url = i.get("href")
    alist_all.append(url)

# print(alist_all)
img_list = []
for i in alist_all:
    # print(i)
    # print(i.strip('/'))
    resp1 = get_page(i)
    # print(resp1)
    
    img = resp1.find("div",class_="ImageBody").find("img")
    img_src  = img.get('src')
    img_name = img_src.split("/")[-1]

    img_resp = requests.get(img_src)

    with open('./pict/'+img_name,mode='wb') as f:
        f.write(img_resp.content)

    print("over!",img_name)
    time.sleep(1)

print("all over!!")
    
    
