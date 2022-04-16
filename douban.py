import requests
import re
import csv
import time

# https://movie.douban.com/top250?start=25&filter=
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36'
}
f=open("douban.csv",mode="w")
csvwrite = csv.writer(f)

for i  in range(10):
    uri = f'https://movie.douban.com/top250?start={i*25}&filter='
    resp = requests.get(uri,headers = headers)
    result_content = resp.text
    resp.close()

    obj = re.compile(r'<li>.*?<div class="item">.*?<a href="(?P<href>.*?)">.*?<img width=.*?'
    r'src="(?P<img>.*?)".*?<span class="title">(?P<movie>.*?)</span>.*?<p class="">(?P<dictor>.*?)&nbsp.*?<br>(?P<year>.*?)&nbsp'
    r'.*?<span class="rating_num" property="v:average">(?P<pingfen>.*?)</span>.*?<span>(?P<total>.*?)人评价</span>'
    r'.*?<span class="inq">(?P<solan>.*?)</span>',re.S)

    result = obj.finditer(result_content)
    for i in result:
        print(i.group("movie"))
        data = i.groupdict()
        data['dictor'] = data['dictor'].strip()
        data['year'] = data['year'].strip()
        csvwrite.writerow(data.values())
f.close()



