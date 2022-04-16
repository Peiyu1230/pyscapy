# from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains



# web = webdriver.ChromeOptions()

# web.add_argument("user-agent=Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1")

# browser = webdriver.Chrome(chrome_options=web)
# browser.get("https://bean.m.jd.com")
# print(browser.page_source)
# # browser.quit()
driver = webdriver.Chrome()
driver.set_window_size(480,800)

web.quit()




