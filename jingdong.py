import requests

'''
1\获取activ id
2、 activityId: b2cc054e43414cdba52874a116fbf0bc  已知
    pin: B6EmAJ2BxisvLiTSFNnSA2wklxRrP5C78lmKjh9Mn4avAmNuF4i+OHS9NlRdtagP 不知道怎么得来   AUTH_C_USER
    productId: 100028020272 已知的


fromType: "WeChat"
token: "2DC08BA2FD6740958700A505C44466182858D47D22D4567CF40B026BBD7BF0F9"
userId: "1000000264"

'''

def get_pin():
    uri = 'https://lzkj-isv.isvjd.com/wxActionCommon/getUserInfo'
    body={

    }
    pass

uri = 'https://lzkj-isv.isvjd.com/customer/getSimpleActInfoVo'
head = {
    "Accept": "application/json",
    "Accept-Encoding": "application/gzip",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "43",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "__jdv=244349341%7Cdirect%7C-%7Cnone%7C-%7C1648441923420; __jdc=244349341; mba_muid=16484419234201225129786; __jda=244349341.16484419234201225129786.1648441923.1648819796.1648823479.4; AUTH_C_USER=B6EmAJ2BxisvLiTSFNnSA2wklxRrP5C78lmKjh9Mn4avAmNuF4i+OHS9NlRdtagP; __jd_ref_cls=Mnpm_ComponentApplied;lz_wq_auth_token=0F59B62F786A060ECCBCA2CB3C8B601B2858D47D22D4567CF40B026BBD7BF0F9; LZ_TOKEN_KEY=lztokenpage184ce5b7bf1e422e8144f9f31f8bd2af; __jdb=244349341.7.16484419234201225129786|4.1648823479; mba_sid=16488234794356175743446409498.7; JSESSIONID=228E8FCED0AD8E20DAADAD7054DC2093; LZ_TOKEN_VALUE=oR/A0k2Svv2JYmhRbAwgyw==",
    "Host": "lzkj-isv.isvjd.com",
    "Origin": "https://lzkj-isv.isvjd.com",
    "Pragma": "no-cache",
    # "Referer": "https://lzkj-isv.isvjd.com/wxCollectionActivity/activity2/b2cc054e43414cdba52874a116fbf0bc?activityId=b2cc054e43414cdba52874a116fbf0bc",
    # Sec-Fetch-Dest: empty
    # Sec-Fetch-Mode: cors
    # Sec-Fetch-Site: same-origin
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1"
}
data = {
    "activityId":"b2cc054e43414cdba52874a116fbf0bc"
}
# s = requests.Session()
# resp = s.post(uri,headers=head,data=data)

# print(resp.request.headers)

# uri = 'https://lzkj-isv.isvjd.com/customer/getSimpleActInfoVo'
'''
{
    "result": true,
    "data": {
        "activityId": "b2cc054e43414cdba52874a116fbf0bc",
        "jdActivityId": 2290214,
        "venderId": 1000000264,
        "shopId": 1000000264,
        "activityType": 6
    },
    "count": 0,
    "errorMessage": ""
}
'''
s = requests.Session()
resp = s.post(uri,headers = head,data=data)

print(resp.headers)

