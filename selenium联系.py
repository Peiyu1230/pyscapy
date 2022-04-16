from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

web = Chrome()


web.get("http://www.lagou.com")

web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a').click()

web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python",Keys.ENTER)
time.sleep(3)
li_list = web.find_elements_by_xpath('//*[@id="jobList"]/div[1]/div')


for i in li_list:
    try:
        job_name = i.find_element_by_xpath("./div/div/div/a").text
        print(job_name)
        job_price = i.find_element_by_xpath("./div/div/div[2]/span").text
        print(job_name,job_price)
    except Exception as e:
        pass
web.quit()