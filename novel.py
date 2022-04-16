
import requests
import asyncio
import aiohttp
import json
import aiofiles

# https://dushu.baidu.com/api/pc/getDetail?data={"book_id":"4306063500"} title cid

# https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}


async def download_page(c_id,b_id,title):
    data={
        "book_id":b_id,
        "cid":f"{b_id}|{c_id}",
        "need_bookinfo":1
    }
    data = json.dumps(data)
    url = f"https://dushu.baidu.com/api/pc/getChapterContent?data={data}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dict = await resp.json()
            # print(dict)
            async with aiofiles.open("novel/"+title+'.txt','w') as f:
               await f.write(dict['data']['novel']['content'])

async def main(uri):
    resp = requests.get(uri)
    dict = resp.json()
    tasks = []
    for i in dict['data']['novel']['items']:
        title = i['title']
        cid = i['cid']
        tasks.append(download_page(cid,b_id,title))
        # 调用协程
      
    await asyncio.wait(tasks)





if __name__ == "__main__":
    b_id = '4306063500'
    uri = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"%s"}'%(b_id)
    asyncio.run(main(uri)) 