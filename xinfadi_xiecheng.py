import asyncio
import aiohttp
import aiocsv
import aiofiles
import csv



async def download(url,body,f):
    print("start")
    async with aiohttp.ClientSession() as seesion:
        async with seesion.post(url,data=body) as resp:
            dict = await resp.json()
            async for i in dict['list']:
                name =  i['prodName']
                lowPrice =  i['lowPrice']
                highPrice =  i['highPrice']
                avgPrice =  i['avgPrice']
                specInfo =  i['specInfo']
                pubDate =  i['pubDate'].split(" ")[0]
                # async with aiofiles.open(f'csv/{title}.csv','a') as f:
                #     await f.write(str([name,lowPrice,highPrice,avgPrice,specInfo,pubDate]))
                #     await f.write('\n')
                await f.write((str([name,lowPrice,highPrice,avgPrice,specInfo,pubDate])))
                await f.write('\n')

    print("end")

async def get_page(url):
    tasks = []
    with open("./csv/xinfadi_.csv",'w') as f:
        for i in range(1,20):
            data = {
                "limit": 20,
                "current": i
            }
            tasks.append(download(url,data,f))
        await asyncio.wait(tasks)

if __name__ == "__main__":
    uri = 'http://www.xinfadi.com.cn/getPriceData.html'
    asyncio.run(get_page(uri))
