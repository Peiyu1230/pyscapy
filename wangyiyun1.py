import requests
from Crypto.Cipher import AES
import json
from base64 import b64encode

headers = {
    "referer": "https://music.163.com/song?id=1928857203"
    # "User-Agent:":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36"
}
uri = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='

'''
e2x.method = "post";
            delete e2x.query;
            var bMq9h = window.asrsea(JSON.stringify(i2x), bsy7r(["流泪", "强"]), bsy7r(Xk1x.md), bsy7r(["爱心", "女孩", "惊恐", "大笑"]));
            e2x.data = j2x.cr2x({
                params: bMq9h.encText,
                encSecKey: bMq9h.encSecKey
            })
'''
e = '010001'
#  bsy0x(Xk6e.md)=      "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
# bsy0x(["爱心", "女孩", "惊恐", "大笑"]) = "0CoJUm6Qyw8W8jud"
g= '0CoJUm6Qyw8W8jud'

i = "Wf6kAtyWRsr3oHCf" #固定 seckey就固定了

'''
function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)  16位随机数
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) { a i2x b 0CoJUm6Qyw8W8jud
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708") iv = 0102030405060708
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
function c(a, b, c) { a 16位随机数 b 010001 c ''
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) { d = i2x e = 010001 f =  g = 0CoJUm6Qyw8W8jud
        var h = {}
          , i = a(16);  i为16位随机数  "goGbfLb4LtdEAXJY"
        return h.encText = b(d, g), 
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f), c
        h
    }
    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }
    window.asrsea = d,
'''
data1 = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1928857203",
    "threadId": "R_SO_4_1928857203"
}


def get_encSecKey():
        return "de74823dbca777ffeefcaf6fda60f8832d528da78c06df322b307f004003099fcea7ef0bd98ff7eb335088fe31bdb05d31230bd7e397c7984c7ae96e603fe11dabc84f7c70ed73a535f7dc416b6c72e01144a0233afa4c2366d29ce0022188b2904a1bfecfb9a8026c1ae796b15a7d6cb0eb8b40e0c244929c1747c596bce0ff"

def to_16(data):
    le = 16 - len(data)%16
    data += chr(le)*le
    # print(type(data))
    return data


def get_encText(data):
    first = encText(data,g)
    second =encText(first,i)
    return second

def encText(data,key):
    iv="0102030405060708"
    data=to_16(data)
    aes=AES.new(key=key.encode('utf-8'),
                IV=iv.encode('utf-8'), mode=AES.MODE_CBC)
    bs=aes.encrypt(data)
    return str(b64encode(bs), 'utf-8')
    
    





result = {
    "params" : get_encText(json.dumps(data1)),
    "encSeckey":get_encSecKey()
}
print(type(result))
resp = requests.post(uri,headers = headers,data = result)

print(resp.text)

