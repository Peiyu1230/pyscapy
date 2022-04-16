import requests
import asyncio
import aiohttp
import aiofiles
import re
from  Crypto.Cipher import AES
import os







# 4、合并视频
def download_page(url,name):
    resp = requests.get(url,verify =False)
    with open(f"./m3u/{name}","w") as f:
        f.write(resp.text)
    print("m3u8文件下载完成")
    return resp

async def down_ts(i,session):
    name = i.rsplit("/",1)[1]
    async with session.get(i,headers=header) as resp:
        async with aiofiles.open(f'./m3u/{name}',"wb") as f:
            await f.write(await resp.content.read())

    print(f'{name}已下载完成！！！')

async def down_m3u():
    # https://qq.shanshanku.com/20220322/nttls2yx/hls/oYg23XEe.ts
    tasks = []
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open ("./m3u/获取m3u文件.txt",'r',encoding="utf-8") as f:
                async for i in f:
                    if i.startswith("#"):
                        continue
                    i = i.strip()
                    # print(i)
                    task = asyncio.create_task(down_ts(i,session))
                    tasks.append(task)
                await asyncio.wait(tasks)


async def jiema_ts(name,key):
    aes = AES.new(key=key,IV=b"0000000000000000",mode=AES.MODE_CBC)
    async with aiofiles.open(f"./m3u/{name}",'rb') as f1,\
        aiofiles.open(f"./m3u/temp_{name}",'wb') as f2:
        bs = await f1.read()
        await f2.write(aes.decrypt(bs))

    print(f"{name}解密完成")

    


async def aio_dec(key):
    # 读取文件名称，
    tasks = []
    async with aiofiles.open("./m3u/获取m3u文件.txt",'r',encoding="utf-8") as f:
        async for i in f:
            if i.startswith("#"):
                continue
            i = i.strip()
            name = i.rsplit("/",1)[1]
            # print(name)
            task = asyncio.create_task(jiema_ts(name,key))
            tasks.append(task)
            
        await asyncio.wait(tasks)
    # 遍历解密

def merge_ts():
    name_list = []
    with open("./m3u/获取m3u文件.txt","r",encoding='utf-8') as f:
        for name in f:
            if name.startswith("#"):
                continue
            name = name.rsplit("/",1)[1].strip()

            name_list.append(f'./m3u/temp_{name}')
    s = " ".join(name_list)
    os.system(f'cat {s} > 步步惊心.mp4')


def main(url):
    print("开始========")
    # 1.找到页面云代码
    resp =requests.get(url,headers = header,verify = False)
    print(resp.text)
    obj = re.compile(r'},"url":"(?P<uri>.*?)",',re.S)
    # 找到视频播放链接
    domain_url = obj.search(resp.text).group("uri")

    # 2。1、第一次请求链接 得到第一次m3u地址
    dic = download_page(domain_url.replace("\\",""),"获取原m3u地址.txt")
    # /20220322/nttls2yx/hls/index.m3u8
    first_url = dic.text.split("/",1)[1].strip()

    main_url = "https://qq.sd-play.com/"
    # 2。2、第二次请求链接 得到第一次m3u地址
    second_url = main_url + first_url
    # print(second_url)
    download_page(second_url,"获取m3u文件.txt")

    # 3、下载视频
    asyncio.run(down_m3u())

    # 4 拿到秘钥
    key_uri = "https://qq.shanshanku.com/20220322/nttls2yx/hls/key.key"
    key  = download_page(key_uri,"key.text").text
    print(key)
    # 4.aec解密
    asyncio.run(aio_dec(key))

    # 5 合并
    merge_ts()
        


if __name__ == "__main__":
    uri = 'https://www.pkmp4.com/py/58169-4-1.html'
    header={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36"
    }
    main(uri)