# [rule: ] 



import requests
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NTA4MDI0NzMzMSwiaWF0IjoxNjQ4OTk2NzM0LCJleHAiOjE2ODA1MzI3MzR9.pq9kwNpLo9fA-plxghrXc0GANxEVChjvK6wZctSJWOY'

header={
    'Authorization': 'Bearer ' + token
}
data = {
    "code":"10:/￥H4CuiDaraB￥，分京豆这件事怎能少了你，快来成为我的队员一起瓜分京豆吧！"
}

resp = requests.post('https://api.jds.codes/jd/jcommand',headers = header,data=data).json()
url = resp['data']['jumpUrl'].split("&")[0]
print(url)
