import requests
import json
import re

#请求地址
url = 'https://www.kuaishou.com/graphql'
headers = {
"content-type": 'application/json',
    "Cookie": 'kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; did=web_d5468278a1e92934b3751f249005ffd3; client_key=65890b29; userId=1002026148; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABb3k7H6FPn5rPTxi_U90A1EyivbCG1lWIL1_rV6NDVpXzhBc1jBu7ym59g3fUExHe5ZNBf8YKAXnF2IL0cRoE0cCKrTTndeqWCsDxF5FFXwEjJVAWhZTi87lyyhTvvOBDBgG7AZ03thuTfr_QXmvbueTi9Yd_RBKwIWhWZ9cY88tn8OqN_4iX9l7mHh7PvK7eCnL3BXSM0JABpysi1936rxoS1KQylfZfbCBEuMI0IcjfqenKIiBZWJZqfmVkyM3JqsKIBJh0A-rz8bGOJ_hOfif7PIQInSgFMAE; kuaishou.server.web_ph=4185d09841f87d0bcad53e5c0029de4c6304',
    "Host": 'www.kuaishou.com',
    "Origin": 'https://www.kuaishou.com',
    "Referer": 'https://www.kuaishou.com/search/video?searchKey=%E6%80%A7%E6%84%9F',
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
}
data = {
    "operationName": "visionSearchPhoto",
    "variables": {"keyword": "小姐姐", "pcursor": "", "page": "search"},
    "query": "query visionSearchPhoto($keyword: String, $pcursor: String, $searchSessionId: String, $page: String, $webPageArea: String) {\n  visionSearchPhoto(keyword: $keyword, pcursor: $pcursor, searchSessionId: $searchSessionId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      type\n      author {\n        id\n        name\n        following\n        headerUrl\n        headerUrls {\n          cdn\n          url\n          __typename\n        }\n        __typename\n      }\n      tags {\n        type\n        name\n        __typename\n      }\n      photo {\n        id\n        duration\n        caption\n        likeCount\n        realLikeCount\n        coverUrl\n        photoUrl\n        liked\n        timestamp\n        expTag\n        coverUrls {\n          cdn\n          url\n          __typename\n        }\n        photoUrls {\n          cdn\n          url\n          __typename\n        }\n        animatedCoverUrl\n        stereoType\n        videoRatio\n        __typename\n      }\n      canAddComment\n      currentPcursor\n      llsid\n      status\n      __typename\n    }\n    searchSessionId\n    pcursor\n    aladdinBanner {\n      imgUrl\n      link\n      __typename\n    }\n    __typename\n  }\n}\n"
}
#将字典转换为json格式
data=json.dumps(data)
#发送请求获取数据
response=requests.post(url,headers=headers,data=data)
resp=response.json()['data']['visionSearchPhoto']['feeds']
# 遍历拿到每一条
for feed in resp:
    #每条视频的文案
    caption=feed['photo']['caption']
    new_caption = re.sub(r'[\/:*?"<>|\n\\]', '_', caption)
    #每条视频的视频地址
    photoUrl=feed['photo']['photoUrl']
    # 请求没事视频的地址.content是二进制视频
    rsp = requests.get(photoUrl).content
    # 下载视频
    with open('video\\' + new_caption + '.mp4', mode='wb') as f:
        f.write(rsp)
    print(caption, '下载完成')