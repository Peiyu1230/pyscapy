import requests
import re
import csv


f = open('shenme.csv',mode="w",encoding="utf-8")
csvwrite = csv.writer(f)


uri = "https://www.smzdm.com/p/50613732/"
headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36'
}

resp = requests.get(uri,headers = headers)
result_content = resp.text
resp.close()
obj = re.compile(r'<tr>.*?<a.*?href="(?P<href>.*?)".*?<td.*?>(?P<title>.*?)</td>.*?</tr>')
result = obj.finditer(result_content)

for it in result:
    # print(it.group("href"))
    # print(it.group("title"))
    data = it.groupdict()
    csvwrite.writerow(data.values())

f.close()