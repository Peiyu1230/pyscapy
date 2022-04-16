import requests
import json
from urllib.parse import quote
import asyncio
import aiohttp
import aiofiles




async def download(uri,name):
    async with aiohttp.ClientSession() as session:
        async with session.get(uri,headers= header) as resp:
            async with aiofiles.open(f"video/{name}.MP4",'wb') as f:
                await f.write(await resp.content.read())

async def check_url(resp):
    tasks=[]
    for i in resp['data']:
        print(type(i))
        try:
            dic = i['aweme_mix_info']['mix_items']
        except Exception as e:
            break
        for j in dic:    
            title = j['desc']
            url = j['video']['download_addr']['url_list'][0]
            task = asyncio.create_task(download(url,title))
            tasks.append(task)
    await asyncio.wait(tasks)
name = "风景"
keyname = quote(name)
uri = f'https://www.douyin.com/aweme/v1/web/general/search/single/?device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_general&sort_type=0&publish_time=0&keyword={keyname}&search_source=normal_search&query_correct_type=1&is_filter_search=0&from_group_id=&offset=0&count=15&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=100.0.4896.75&browser_online=true&engine_name=Blink&engine_version=100.0.4896.75&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7079409696313984526&msToken=_hwCpTlTmKfp-FtghoKJGJmEzsw1C16TWA4bRKdTcc2r4xMdVkjBz9qSa9-0ZNq5ySRFmkbB2eKSirD07tiNxFsz4h3x4_zxnPqWuyvIjIFf_zuWReApCVBvmWW_7gI=&X-Bogus=DFSzswVunPsANx1-SARukr7Tlqtv&_signature=_02B4Z6wo000018hdjBgAAIDAXIvXFfHZipvIXYiAAJBOLP2Gdo-b9fcimFj9dOkU2XzC8Lq5v-CKGuTus.o1GyLYDRhlPgG.c2TFVPqax7jrz-fChkOCCp6eNiuGszaRR8J3Pds7I8fBY6MHdd'
header = {
    # "cookie":"NVE4h4Vyto; sso_uid_tt=07c6fec9b693b61a488de8fd47830c9f; sso_uid_tt_ss=07c6fec9b693b61a488de8fd47830c9f; toutiao_sso_user=16158bee25e49d2e009e4322aa9bab6d; toutiao_sso_user_ss=16158bee25e49d2e009e4322aa9bab6d; sid_ucp_sso_v1=1.0.0-KGRhMDYxYjA4ZDcyMTc1NGU1YzkwZWQyNjM1NDI1NzU2OTg0YzA3OTYKHQjakfzoiwIQws3LkgYY7zEgDDCvx_fOBTgGQPQHGgJsZiIgMTYxNThiZWUyNWU0OWQyZTAwOWU0MzIyYWE5YmFiNmQ; ssid_ucp_sso_v1=1.0.0-KGRhMDYxYjA4ZDcyMTc1NGU1YzkwZWQyNjM1NDI1NzU2OTg0YzA3OTYKHQjakfzoiwIQws3LkgYY7zEgDDCvx_fOBTgGQPQHGgJsZiIgMTYxNThiZWUyNWU0OWQyZTAwOWU0MzIyYWE5YmFiNmQ; odin_tt=8d304a1606988570288996e11e6502b5f07ab7ba424ed71c9de10757249c4b44bf546f75c392a88396188bd462c88dbb; sid_guard=16158bee25e49d2e009e4322aa9bab6d%7C1649600195%7C5184000%7CThu%2C+09-Jun-2022+14%3A16%3A35+GMT; uid_tt=07c6fec9b693b61a488de8fd47830c9f; uid_tt_ss=07c6fec9b693b61a488de8fd47830c9f; sid_tt=16158bee25e49d2e009e4322aa9bab6d; sessionid=16158bee25e49d2e009e4322aa9bab6d; sessionid_ss=16158bee25e49d2e009e4322aa9bab6d; sid_ucp_v1=1.0.0-KGZhMGU5NjA5Nzg5ZDU5N2YzNzkxNTFhNDQ1ZTRkNDI5NWQ1ZGI0ZjAKHQjakfzoiwIQw83LkgYY7zEgDDCvx_fOBTgGQPQHGgJobCIgMTYxNThiZWUyNWU0OWQyZTAwOWU0MzIyYWE5YmFiNmQ; ssid_ucp_v1=1.0.0-KGZhMGU5NjA5Nzg5ZDU5N2YzNzkxNTFhNDQ1ZTRkNDI5NWQ1ZGI0ZjAKHQjakfzoiwIQw83LkgYY7zEgDDCvx_fOBTgGQPQHGgJobCIgMTYxNThiZWUyNWU0OWQyZTAwOWU0MzIyYWE5YmFiNmQ; __ac_nonce=06252e6c300a8efbf2ac5; _tea_utm_cache_2018=undefined; FOLLOW_LIVE_POINT_INFO=MS4wLjABAAAARxeNEedfDwZnBSkh6JtJ0oufkecTDKp8qa8c6a5DiuU%2F1649606400000%2F0%2F1649600204534%2F0; _tea_utm_cache_2285=undefined; msToken=cruvkCZo0-1KzzBF-mKnp5DMKkEO_0RW7lMjQTcANLdA1DUfA6gvC0vYWkfBMP6Ky3iluOW9Ttf1_VMDng6SuVqikaq6udfG26wPbxT14H7hSiRztne7nQ==; home_can_add_dy_2_desktop=1; tt_scid=yjxK7yb.qHisxD5QsDEj1kcwcqiiUBLSM-hXjoErhJDT-YZDr5SRa-tpwkwQU6yWbb39; pwa_guide_count=2; THEME_STAY_TIME=299519; IS_HIDE_THEME_CHANGE=1; msToken=_hwCpTlTmKfp-FtghoKJGJmEzsw1C16TWA4bRKdTcc2r4xMdVkjBz9qSa9-0ZNq5ySRFmkbB2eKSirD07tiNxFsz4h3x4_zxnPqWuyvIjIFf_zuWReApCVBvmWW_7gI=",
    "referer":f"https://www.douyin.com/search/{keyname}?aid=9b83f210-e680-4a0e-8954-97b425c86c69&publish_time=0&sort_type=0&source=normal_search&type=general",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
}

resp = requests.get(uri,headers=header).json()

# dic = resp['data'][0]
# url = dic['aweme_mix_info']['mix_items'][0]['video']['download_addr']['url_list'][0]

asyncio.run(check_url(resp)) 





