# 1\获取页面源代码
# 2、获取m3u地址
# 3、请求m3u地址 获取m3u
# 4、下载 切片
# 5、合并视频

import requests
import re
import time

# uri = 'https://91kanju.com/vod-play/61543-2-1.html'
header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36"
}
# resp = requests.get(uri,headers = header,verify=False)
# # print(resp.text)
# obj = re.compile(r"url: '(?P<uri>.*?)',",re.S)
# m3u_uri = obj.search(resp.text).group("uri")
# # 处理跳转
# resp.close()
# resp1 = requests.get(m3u_uri,headers = header,verify=False)
# zhenshi = resp1.text
# resp1.close()
# u = zhenshi.split('/',1)[1].strip()

# final_m3u = "https://new.iskcd.com/" + u
# # print(final_m3u,m3u_uri)
# # 下载m3u文jian
# # time.sleep(3)
# resp2 = requests.get(final_m3u,headers = header,verify=False)
# # print(resp2.text)
# with open("./m3u/超高跟.m3u8",'wb') as f:
#     f.write(resp2.content)
# resp2.close()


# xiazai 
n=1
with open('./m3u/超高跟.m3u8',"r",encoding="utf-8") as f:
    for i in f:
        i = i.strip()
        if i.startswith("#"):
            continue


        resp = requests.get(i,headers = header,verify = False)
        f = open(f'./video/{n}.ts','wb')
        f.write(resp.content)
        f.close()
        resp.close()
        print(f"完成{n}个")
        n += 1
        


