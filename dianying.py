import requests
import re
import csv

uri = "https://www.dy2018.com/"

f = open('dianying.csv',mode='w',encoding='utf-8')
csvw = csv.writer(f)

resp = requests.get(uri,verify=False)
resp.encoding = 'gb2312'

# 1/
obj = re.compile(r'2022必看热片.*?<ul>(?P<all>.*?)</ul>',re.S)
obj1 = re.compile(r"<a href='(?P<herf>.*?)'",re.S)
obj2 = re.compile(r'◎片　　名(?P<name>.*?)<br />.*?'
r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<magnet>.*?)"',re.S)


result = obj.finditer(resp.text)

url_li = []
for it in result:
    ul = it.group('all')

    resu = obj1.finditer(ul)
    for i in resu:
        u = i.group('herf').strip('/')
        url = uri+u
        url_li.append(url)
# print(url_li)

# 获取页面内的链接
for i in url_li:
    content = requests.get(i,verify=False)
    content.encoding='gb2312'
    result1 = obj2.search(content.text)
    xx = result1.groupdict()
    csvw.writerow(xx.values())







f.close()