import requests
import time

    
time_ = int(time.time())

coo = '_ga=GA1.1.1757353367.1623169565; Hm_lvt_56cd01307dc3c795bb735a379cdc5e35=1647954930; huoduan_wechat_fans=7a2f28f62733531926df645d3b1e4de9; _ga_30MWTMG29B=GS1.1.{}.24.1.1648303718.0; b2_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lmtlaml3YW5qaWEuY29tIiwiaWF0IjoxNjQ4MzQ2NjgwLCJuYmYiOjE2NDgzNDY2ODAsImV4cCI6MTY0OTEyNDI4MCwiZGF0YSI6eyJ1c2VyIjp7ImlkIjoiMTU0NTMifX19.0ZyID7kyhNusvgBuePkeRskiEBymPLJCDEzufJqrGuA; wordpress_logged_in_319c49a2ee14e4fe558a6454d059be91=user15453_107%7C1648519480%7CWUEP8cNav9fpd7UhdXx2B2LDdOskI8GDM7lYFA6X5c6%7Cb8da8510649812e1e3c3d91e3d3eeb114aec1f79c3a62d8c1cf062048475d8b7; _ga_82DHH1SNHE=GS1.1.1648346594.65.1.1648346796.0; Hm_lpvt_56cd01307dc3c795bb735a379cdc5e35=1648346797; wprus_user_pending_async_actions=OeUeMRtCvM3KFKFDTPsaSQjft1zpIdQM74CwNbDl2w7AfD7WWsh5WucWdbZkLAeMtIG2lmfJFCNLl6C_RVFiXw%3D%3D'.format(str(time_))
hearders={
'Content-Length': '0' ,
'Pragma': 'no-cache' ,
'Cache-Control':'no-cache' ,
'Accept': 'application/json, text/plain, */*' ,
'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lmtlaml3YW5qaWEuY29tIiwiaWF0IjoxNjQ4MzQ2NjgwLCJuYmYiOjE2NDgzNDY2ODAsImV4cCI6MTY0OTEyNDI4MCwiZGF0YSI6eyJ1c2VyIjp7ImlkIjoiMTU0NTMifX19.0ZyID7kyhNusvgBuePkeRskiEBymPLJCDEzufJqrGuA' ,
'sec-ch-ua-mobile': '?0' ,
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36' ,
'Origin': 'https://www.kejiwanjia.com' ,
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8' ,
'Cookie':  coo,
}

res = requests.post('https://www.kejiwanjia.com/wp-json/b2/v1/userMission',headers = hearders)
print(res.status_code)
# 调用wxpusher
head = {"Content-Type":"application/json"}
body = {"appToken":"AT_Ubp19R8ufENVAadukEgEFXaC548Af4zK","content":"科技玩家签到成功","summary":"消息摘要","contentType":1, "topicIds":[],"uids":["UID_htGFMK8IO08sOHIpJ2b1Rgi8GEYH"],"url":""}

resp = requests.post("http://wxpusher.zjiecode.com/api/send/message",headers = head,json = body)
print(resp.text)