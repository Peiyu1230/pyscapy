import requests

from Crypto.Cipher import AES
from base64 import b64encode
import json

uri = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='


headers = {
    "referer": "https://music.163.com/song?id=1928857203"
    # "User-Agent:":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36"
}

# post


# data
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

# bmq3x
# params = encSecKey: "bb809f72c082f97bb9f8785a79a45748793f120d34506c55603273fb9b627252463e65e7c62e75c6776a788e4b9a75abad7dfc43297deb19e51e9eb192e31e3117aafcbe6fe73c9b494b6dce40ab33f87d318da5eb59c2dc9670ca8ea56f7c1dafdd9ad24b85cafc156221ff4f1b9b91c2cdc31a710ab66bd81cd2915add17e4"
# encsecKey = encText: "vVSljbo70ZuNv3AOoppqg6IYj6XsoYamkb5IgV3dzBaAyQR/6bNkC8p4Yd5pNCAZIpeF2QdH0qdqPNZQpF5Gs7w86+DbZza6Cfb7NBHF5rq3Y3ik9lrKl1HFLj8m7lOne75Nymb6ePPDXPp+ORFV3IiV8Y9pvcv+Yh4+wLJu3EmNW2z0d+4xQOd/EscGCfJkVHTKz7d90JKU9CSsTX3W1MXKYWaT777c71pI1eWPHMJVXaDGgsueDCzifIO2BLha+22r5CULooB+thGW5XKVtdQhIQJuqdYgLPWTNk6e4tk="

"""
    function a(a) #返回随机的16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) { a是data b是16位字符串
        var c = CryptoJS.enc.Utf8.parse(b) c也是字符串
          , d = CryptoJS.enc.Utf8.parse("0102030405060708") d是字符串
          , e = CryptoJS.enc.Utf8.parse(a)  e是data
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16); #16位随机字符串
        return h.encText = b(d, g),
        h.encText = b(h.encText, i), #返回的是parames
        h.encSecKey = c(i, e, f), #得到的是seckey
        h
    }
    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }
    window.asrsea = d,
"""

# var bMq3x = window.asrsea(JSON.stringify(i9b), bsy0x(["流泪", "强"]), bsy0x(Xk6e.md), bsy0x(["爱心", "女孩", "惊恐", "大笑"]));
# d(d, e, f, g)
# bsy0x(["流泪", "强"])=010001
e = '010001'
#  bsy0x(Xk6e.md)=      "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
# bsy0x(["爱心", "女孩", "惊恐", "大笑"]) = "0CoJUm6Qyw8W8jud"
g = '0CoJUm6Qyw8W8jud'

i = "Mis2i6bHW9sYhyRm"  # 固定 seckey就固定了


def get_seckey():
    return "0993207b27c7a44bb43379db28a2e00c1d192cff9974a6a755e1c077ce067abbf5b16f9a8214c0ef608bf42fdcf800a8ba4f4a23e5e8211a57abdd7fb9cdcede3e916886f95ac1fde403dcb9deeb344b7bb806124adf050742161249518837df5de82dc1a9c593abc983f57e74824533ed22fca4662850c6e248845475291711"


def get_params(data):
    # return h.encText = b(d, g),
    # h.encText = b(h.encText, i),

    first = enc_params(data, g)
    second = enc_params(first, i)
    return second


def to_16(data):
    le = 16-len(data) % 16
    data += chr(le) * le
    # print(len(data)
    return data

def enc_params(data, key):  # data必须是字符串
    iv="0102030405060708"
    data=to_16(data)
    aes=AES.new(key=key.encode('utf-8'),
                IV=iv.encode('utf-8'), mode=AES.MODE_CBC)
    bs=aes.encrypt(data)
    return str(b64encode(bs), 'utf-8')

resp=requests.post(uri, headers=headers, data={
    "params": get_params(json.dumps(data1)),
    "encSecKey": get_seckey()
})
print(resp.text)
