import requests
import json
import asyncio
import aiohttp
import aiofiles
from concurrent.futures import ThreadPoolExecutor
import random

from urllib.parse import quote,unquote


uri = 'https://weibo.com/tv/api/component?page=%2Ftv%2Fhot'
uri1 = 'https://weibo.com/tv/show/'
data={'data':'{"Component_Home_Hot":{"count":18,"next_cursor":""}}'}


header = {
    # WBStorage=4d96c54e|undefined; 
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    'referer': 'https://weibo.com/tv/hot',
    'cookie':'SUB=_2AkMVBelKf8NxqwJRmP0Szmrmb4xyzAjEieKjWRiRJRMxHRl-yT8Xqm0jtRB6PoXHpQ-7FR6wdkTTL-0gRvxHM7UKqXLi; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWwuLXuaGPrJMr1DSs_zeSb; login_sid_t=14f96491cf2f15f031df59c0f56c6b3f; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; wb_view_log=1440*9002; TC-V-WEIBO-G0=35846f552801987f8c1e8f7cec0e2230; Apache=8121162574416.35.1650026113730; SINAGLOBAL=8121162574416.35.1650026113730; ULV=1650026113979:1:1:1:8121162574416.35.1650026113730:; XSRF-TOKEN=HyWxpwQKERr7PRTnf9zG8Atl; WBPSESS=a_YZA6I5qCR3U8i3Rfvlpj-Qi6fqWVRjQmC-DGdR35wRgELCtTmwAqJEE_19AHhu7UlNNlO5_VA2ZGKCcPppipynEqvoM7KaeewBlu6aJtplELt7IOEKBpCf7EuKLhgc',
    'page-referer':'/tv/home'
}

def get_video_url():
    url_list = resp['data']['Component_Home_Hot']['list']
    url_dict=[]
    for i in url_list:
        url =uri1 + i['oid']+'?mid='+str(i['media_id'])
        url_dict.append(url)
    return url_dict


async def down_video(url,name,session):

    async with aiofiles.open(f"video/{name}.mp4",'wb')as f:
        async with session.get('https://'+url,headers=header) as resp:
            await f.write(await resp.content.read())
    print(f"正在写入{name}")

async def down(resp_all):
    print("开始下载=======")
    tasks =[]
    async with aiohttp.ClientSession() as session:
        for resp in resp_all:
            down_url = resp['data']['Component_Play_Playinfo']['urls']['高清 1080P']
            title = resp['data']['Component_Play_Playinfo']['title']
            url = down_url.split('//')[1]       
            print(title)
            task = asyncio.create_task(down_video(url,title,session))
            tasks.append(task)
        await asyncio.wait(tasks)


def get_video(url):
    
    reps_list = []
    for u in url:
        header['referer']=u
        uid = u.rsplit('/',1)[1].split('?')[0]
        header['page-referer'] = f'/tv/show/{uid}'
        u2 = f'https://weibo.com/tv/api/component?page=%2Ftv%2Fshow%2F{unquote(uid)}'
        data1 = {'data':'{"Component_Play_Playinfo":{"oid":"%s"}}'%(uid)}
        resp = requests.post(u2,headers=header,data=data1).json()
        reps_list.append(resp)
    return reps_list

def down_test(url):
    print(url)   
    print("==========开始下载==========")
    with open('video/%s.mp4'%random.randint(0,199),'wb') as f:
        resp = requests.get(url)
        f.write(resp.content)




if __name__ == "__main__":
    session = requests.session()
    resp =session.post(uri,headers=header,data=data)
    resp = json.loads(resp.text)
    url_dict = get_video_url()
    # 所有的下载链接
    resp_dict = get_video(url_dict) 
    # asyncio.run(down(resp_dict))
    # 调用线程池，同步下载视频
    # print(resp_dict)
    down_dict=[]
    name_dict=[]
    try:
        for i in resp_dict:
            down_url = i['data']['Component_Play_Playinfo']['urls']['高清 1080P']
            title = i['data']['Component_Play_Playinfo']['title']
            url = down_url.split('//')[1]
            down_dict.append("https://"+url)
            # print(down_dict)
        executor = ThreadPoolExecutor(max_workers=3)
        for data in executor.map(down_test,down_dict):
            print("=====已下载完成1个======")
    except Exception as e:
        
        executor.shutdown()
        print(f"错误了!{e}")

    
