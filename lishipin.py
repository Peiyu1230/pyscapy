import requests

uri = 'https://www.pearvideo.com/video_1756791'

url_id = uri.split("_")[1]
header={
    "Referer": uri,
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36"
}

uri1 = f'https://www.pearvideo.com/videoStatus.jsp?contId={url_id}&mrd=0.6022665161992877'
resp = requests.get(uri1,headers = header)

# 
dict = resp.json()
systemTime = dict['systemTime']
srcUrl= dict['videoInfo']['videos']['srcUrl']
# https://video.pearvideo.com/mp4/adshort/20220329/1648712197938-15852548_adpkg-ad_hd.mp4
# https://video.pearvideo.com/mp4/adshort/20220329/cont-1756791-15852548_adpkg-ad_hd.mp4
src = srcUrl.replace(systemTime,f"cont-{url_id}")

with open(f"./pict/{url_id}.mp4",mode="wb") as f:
    f.write(requests.get(src).content)
    print("over!")
