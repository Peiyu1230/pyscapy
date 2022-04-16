from chaojiying import Chaojiying_Client
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


web = webdriver.ChromeOptions()

web.add_argument("user-agent=Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1")

browser = webdriver.Chrome(chrome_options=web)
browser.get("https://plogin.m.jd.com/login/login?appid=100&returnurl=https%3A%2F%2Fh5.m.jd.com%2Frn%2F2E9A2bEeqQqBP9juVgPJvQQq6fJ%2Findex.html")
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="hello"]/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/div/div[2]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/p[1]/input').clear()
browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/p[1]/input').send_keys("13000000000")
browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/p[2]/button').click()

time.sleep(2)
img = browser.find_element_by_xpath('//*[@id="trackLine"]')
chaojiying = Chaojiying_Client('chaojiying12', '123456', '931248')	#用户中心>>软件ID 生成一个替换 96001
		
# im = open('1.png', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
# print (chaojiying.PostPic(im, 9103))
 
dic = chaojiying.PostPic(img.screenshot_as_png, 9103)
print(dic)
result = dic['pic_str']
r_list = result.split("|")
p_list=[]
for i in r_list:
    p = i.split(",")
    x = int(p[0])
    y = int(p[1])
    p_list.append(x)
    p_list.append(y)
    # ActionChains(browser).move_to_element_with_offset(img,x,y).drag_and_drop_by_offset
ActionChains(browser).move_to_element_with_offset(img,p_list[0],p_list[1]).perform()
time.sleep(0.5)
ActionChains(browser).click_and_hold().perform()
ActionChains(browser).move_to_element_with_offset(img,p_list[2],p_list[3]).perform()
time.sleep(0.5)
ActionChains(browser).move_to_element_with_offset(img,p_list[4],p_list[5]).perform()
time.sleep(0.5)
ActionChains(browser).pause(0.5)


