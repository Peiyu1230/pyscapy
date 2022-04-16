""" PagerMaid module to handle jd command. """

from pagermaid import version
from pagermaid.listener import listener
from pagermaid.utils import lang, alias_command, obtain_message, client
import re
'''
let jumpUrl = data.data.jumpUrl
        let l = jumpUrl.indexOf("//")
        let name = jumpUrl.slice(l + 2, l + 6)
        //console.log(name)

        let i = jumpUrl.indexOf("activityId")
        let j = jumpUrl.indexOf("&", i)
        //console.log(jumpUrl.slice(i + 11, j))

        let k = jumpUrl.indexOf(".com")
        //console.log(jumpUrl.slice(0, k + 4))

        let s = "";
        if (name === "lzkj") {
            let jd_zdjr_activityId = jumpUrl.slice(i + 11, j)
            let jd_zdjr_activityUrl = jumpUrl.slice(0, k + 4)
            s += "export jd_zdjr_activityId=\"" + jd_zdjr_activityId + "\"\n" + "export jd_zdjr_activityUrl=\"" + jd_zdjr_activityUrl+"\""
        } else if (name === "cjhy") {
            let jd_cjhy_activityId = jumpUrl.slice(i + 11, j)
            let jd_cjhy_activityUrl = jumpUrl.slice(0, k + 4)
            s += "export jd_cjhy_activityId=\"" + jd_cjhy_activityId + "\"\n" + "export jd_cjhy_activityUrl=\"" + jd_cjhy_activityUrl+"\""
        }
'''

@listener(is_plugin=False, outgoing=True, command=alias_command("jd_cmd"),
          description="解析 JD 口令",
          parameters="<JD 口令>")

async def jd_cmd(context):
    try:
        text = await obtain_message(context)
    except ValueError:
        return await context.edit("[jd_cmd] " + lang("msg_ValueError"))
    try:
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NTA4MDI0NzMzMSwiaWF0IjoxNjQ4OTk2NzM0LCJleHAiOjE2ODA1MzI3MzR9.pq9kwNpLo9fA-plxghrXc0GANxEVChjvK6wZctSJWOY"       
        header= {"Authorization": "Bearer "+token}
        
        data = (await client.post("https://api.jds.codes/jd/jcommand",headers=header,json={"code": text})).json()
    except:
        return await context.edit("[jd_cmd] 网络错误！")
    if data["code"] != 200:
        return await context.edit("[jd_cmd] 未找到 JD 口令！")
    try:
        data = data["data"]["jumpUrl"]
        
        r = re.compile(r'https://(?P<name>.*?)-isv.*?activityId=(?P<activityId>.*?)',re.S)
        result = r.finditer(data)
        uri = data.split("/")[:3]
        uri = '/'.join(uri)

        for i in result:
            name = i.group('name')
            activityId = i.group("activityId")
            if name in ("lzdz1","lz1d"):
                await context.edit(f'【jd_cmd】export jd_zdjr_activityId = "{activityId}\n"jd_zdjr_activityUrl = "{uri}"')

            elif name == "cjhy":
                await context.edit(f'【jd_cmd】export jd_cjhy_activityId = "{activityId}\n"jjd_cjhy_activityId = "{uri}"')
        
            else:
                await context.edit(f'【jd_cmd】{name}不知道是啥玩应！！！')
            
        #     data = data["data"]["jumpUrl"]
        #     uri = data.split("=")[1].split("&")[0]
        # await context.edit(f'【jd_cmd】export jd_zdjr_activityId = "{uri}"')
    except KeyError:
        return await context.edit("[jd_cmd] 数据错误！")
