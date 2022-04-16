import requests


uri = 'https://translate.volcengine.com/web/dict/match/v1/?msToken=&X-Bogus=DFSzsdVOQDVRQTjrSlgQYN7TlqtA&_signature=_02B4Z6wo00001s3JzyQAAIDBWR-UK1Wz7drNzcuAANFE73tq5ysfoC0eFHiiVYzkMxH7bsM9ffn1DjfTdCwqPrIBL8ki2JtH7mIy9WKTnKPQ2j6j7CPqwpQGFmLyGXI9GxDjzn3JWl7cq2bh04'

resp = requests.post(uri)
resp.encoding="utf-8"
print(resp.text)