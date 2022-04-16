import requests
# from lxml import etree
import json
import csv
import asyncio
import aiohttp


f = open('csv/xinfadi.csv',mode='w',encoding='utf-8')
csvwrite = csv.writer(f)
urls=[
    'http://kr.shanghai-jiuxin.com/file/bizhi/20211201/i2vohgqkcjx.jpg',
    'http://kr.shanghai-jiuxin.com/file/2022/0325/4c594c39041fda293731ce25536a88da.jpg'
]
async def download_page(uri):
    name = uri.rsplit("/",1)[1]
    async with aiohttp.ClientSession() as s:
        async with s.get(uri) as resp:
            
            with open("./pict/"+name,'wb') as f:
                f.write(await resp.content.read())
    # 发送请求
    # 得到图片
    # 保存图片
    print(name,"搞定")
async def main():
    tasks = []

    for i in urls:
        tasks.append(download_page(i))

    await asyncio.wait(tasks)


if __name__ == "__main__":

    asyncio.run(main())

    # with ThreadPoolExecutor(50) as t:
    #     for i in range(1,200):
            
    #         t.submit(download_page('http://www.xinfadi.com.cn/getPriceData.html',i))