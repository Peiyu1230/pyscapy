# get uri
#    获取到LZ_TOKEN_KEY 和 LZ_TOKEN_VALUE
# https://cjhy-isv.isvjcloud.com/microDz/invite/activity/wx/getActivityInfo
#      获取开卡信息
import requests

header = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
    "cookie":"pt_key=AAJiMHXCADAWlb7GJOwyzgVCC46zDB04mnHZetrhrY3yE8kI55AQbb9yvMcwntb_yHufyFN6_s0;pt_pin=13001930827_p;"
}
session = requests.session()
uri = 'https://cjhy-isv.isvjcloud.com/microDz/invite/activity/wx/view/index/4535660?activityId=bf9a9f17deb642ad86ebc2ae1f7d79fc&inviter=x35NT/sPpWjJOpGeOJSsClhXBmEZA6lSVT+72G8p/fVoLg2u1PPhDKnKIGiyllSk&inviterImg=https://img10.360buyimg.com/imgzone/jfs/t1/21383/2/6633/3879/5c5138d8E0967ccf2/91da57c5e2166005.jpg&inviterNickName=abc80808cba&shareuserid4minipg=x35NT%2FsPpWjJOpGeOJSsClhXBmEZA6lSVT%2B72G8p%2FfVoLg2u1PPhDKnKIGiyllSk&shopid=599119'
resp = session.get(uri,headers = header,verify = False)
dic = resp.headers
print(dic)
cookie = dic['Set-cookie']
LZ_TOKEN_KEY = cookie.split(";")[2].split("=")[-1]
LZ_TOKEN_VALUE = cookie.split(";")[5].split("=")[-1]
header1 = {
    "LZ_TOKEN_KEY":LZ_TOKEN_KEY,
    "LZ_TOKEN_VALUE":LZ_TOKEN_VALUE,
    "lz_wq_auth_token":"0CB8F726608065310D57691A9EA6FEC12858D47D22D4567CF40B026BBD7BF0F9"
}
headers = {**header,**header1}
# print(dic)
data = {
    "activityId":"bf9a9f17deb642ad86ebc2ae1f7d79fc"
}
# res = session.post('https://cjhy-isv.isvjcloud.com/microDz/invite/activity/wx/getActivityInfo',headers= headers,verify=False)
# print(res.text)

