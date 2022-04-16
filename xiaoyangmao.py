import requests
from urllib.parse import quote
from urllib.parse import unquote
head = {
        "Cookie":"session_id=KTzh6osux%2BP3p%2FBUI9UVZgXX1WSEuVKKrOSn06KKp7eqEmyilYh8Vw%3D%3D.1648370388;deviceid_md5=d88feef11bee51c76e54547a9016553a;device_s=KTzh6osuxP3p%2FBUI9UVZgXX1WSEuVKKrOSn06KKp7diZot8SED0%2F3rlTVDrD5yGMe4SV60xc%3D;partner_id=0;partner_name=AppStore;device_recfeed_setting=%7B%22homepage_sort_switch%22%3A1%2C%22haojia_recfeed_switch%22%3A1%2C%22other_recfeed_switch%22%3A1%2C%22shequ_recfeed_switch%22%3A1%7D;phone_sort=XR;register_time=1640095983;device_id=KTzh6osux%2BP3p%2FBUI9UVZgXX1WSEuVKKrOSn06KKp7eqEmyilYh8Vw%3D%3D;f=iphone;device_name=iPhone%2011;is_new_user=0;apk_partner_name=appstore;active_time=1640095912;v=10.2.20;device_smzdm_version_code=115;device_smzdm_version=10.2.20;device_system_version=14.2;sess=AT-mnHYquTAmQIZinpXMJZZvmfFaSc5XhqgFG0qc1GZ0JLwj2NvO3YBtr4cM8pvYgpA8f8p3vbFJ0PZHV60zYVmopnk1YV%2BHoqCvoOUKebrvc0XdLyaQf6Oo8Sbkg;login=1;client_id=KTzh6osux%2BP3p%2FBUI9UVZgXX1WSEuVKKrOSn06KKp7eqEmyilYh8Vw%3D%3D.1640095909293;device_idfa=KTzh6osux%2BP3p%2FBUI9UVZjf6%2FwwZ09%2Fupc9HVLeAlFEo2AaZK1SAJQ%3D%3D;osversion=18B92;idfa_md5=0;smzdm_id=4154051331;network=1;device_push=Badge%2C%20Alert%20%26%20Sound;device_type=iPhone12%2C1;ab_test=f;font_size=normal;device_smzdm=iphone;'",
        "User-Agent":"smzdm 10.2.20 rv:115 (iPhone 11; iOS 14.2; zh_CN)/iphone_smzdmapp/10.2.20' "
    }
def getMyPing(uid,token):
    body={
        "userId":"%s"%(uid),
        "token":"%s"%(token),
        "fromType":"APP"
    }
    uri = "https://lzkj-isv.isvjcloud.com/customer/getMyPing"
    res = requests.post(uri,headers = head,data= body)
    print("pin:"+res)
    return res['data']['secrePin']


def getMyToken(actid):
    text = 'body={"to":"https:\/\/lzkj-isv.isvjcloud.com\/activity\/daily\/wx\/indexPage?activityId=","action":"to"}&build=167968&client=apple&clientVersion=10.4.0&d_brand=apple&d_model=iPhone12,1&ef=1&eid=eidIe18581226es18K8iTTKbRQe2h2iUPNio3vCvI8cihjZXcjgQuTVbBAKKg1gL3cfPxDF4s3J6kx00EoentjtTcEnfyxLCvGx4YTmZbu2QBU25FQxS&ep={"ciphertype":5,"cipher":{"screen":"ENS4AtO3EJS=","osVersion":"CJGkCq==","openudid":"ZwSmYtOmCJqyD2Y4CWC2CNTsEQDuYWO0CQG3ENrrDQPsCtDvYzK2CG==","area":"DV8yDNrpCtYyXzG4DNK0","uuid":"aQf1ZRdxb2r4ovZ1EJZhcxYlVNZSZz09"},"ts":1648363537,"hdid":"JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw=","version":"1.0.3","appname":"com.360buy.jdmobile","ridx":-1}&ext={"prstate":"0","pvcStu":"1"}&isBackground=Y&joycious=77&lang=zh_CN&networkType=wifi&networklibtype=JDNetworkBaseAF&partner=apple&rfs=0000&scope=01&sign=056f34f82b8b0c8d494c50065b784abc&st=1648373940584&sv=101&uemps=0-0&uts=0f31TVRjBSshVsyYjTi8qLyLUZc8ebFgmX/jxaO9l4QvKc50YsDUV61aiczqOgbYc32JEjrMXPCzrsvxdRr3t6mJk9789vGXcb89HmIt8L7ewjVmUuT6Oi170kFAS1tg1vzoUIZlJO8Q9kW0 RTKzv7qaR2qndREIsPRkSJ9XSBCcP6y4dmzDSB3io2/hIXk3OwTBoNliSXCltGTXg2xTw=='
    text1 = unquote(text, 'utf-8')
    text2 = text1.replace("activityId=","activityId=%s"%(actid))
    body = quote(text2,'utf-8')

    uri = "https://api.m.jd.com/client.action?functionId=isvObfuscator"
    resp = requests.post(uri,headers = head,data=body)
    print("token:"+resp)
    return resp['token']

def getsuserId(actid):
    uri = 'https://lzkj-isv.isvjcloud.com/customer/getSimpleActInfoVo'
    body = {
        "activityId":"%s"%(actid)
    }
    res = requests.post(uri,headers=body,data=head)
    print("actid:"+res)
    return res['data']['venderId']



if __name__ == "__main__":
    uri = 'https://lzkj-isv.isvjcloud.com/activity/daily/wx/grabGift'
    actid ='4527a62ddc1143719a3ff4ff8366831b'
    uid = getsuserId(actid)
    token = getMyToken(actid)
    pin = getMyPing(uid,token)

    body={
        "actId":actid,
        "pin":pin
    }
    resp = requests.post(url = uri,headers = head, data=body)
    print(resp.text)
