from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time
import os
def browser_initial():
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # browser = webdriver.Chrome(options=chrome_options)
    option = webdriver.FirefoxOptions()
    option.add_argument('headless')
    browser = webdriver.Firefox(options=option)
    browser.maximize_window()
    browser.get('https://www.douyu.com/2550505')
    return browser

def log_csdn(browser):
    #输入你的cookies
    mycookies = os.environ["cookies"]
    listCookies = json.loads(mycookies)

    # 往browser里添加cookies
    for cookie in listCookies:
        cookie_dict = {
            'domain': '.douyu.com',
            'name': cookie.get('name'),
            'value': cookie.get('value'),
            "expires": '',
            'path': '/',
            'httpOnly': False,
            'HostOnly': False,
            'Secure': False
        }
        browser.add_cookie(cookie_dict)
    browser.refresh()

if __name__ == "__main__":
    browser = browser_initial()
    log_csdn(browser)

browser.execute_script('window.scrollTo(0,500)')
time.sleep(8)
#点击背包
browser.find_element_by_xpath('/html/body/div[11]/span').click()
bag = browser.find_element_by_xpath('/html/body/section/main/div[5]/div[1]/div[4]/div[1]/div[2]/div/div[2]/div/div[4]/div/div/span').click()
browser.find_element_by_xpath('/html/body/section/main/div[5]/div[1]/div[4]/div[1]/div[2]/div/div[2]/div/div[4]/div/div/span').click()
time.sleep(2)
#获取礼物数
gift_str = browser.find_element_by_xpath('/html/body/section/main/div[5]/div[1]/div[4]/div[1]/div[2]/div/div[2]/div/div[4]/div/div/div/div[3]/div/div[1]/ul[1]/li[1]/span').text
gift_num = int(gift_str)
#点击礼物
count = 0
while(count<gift_num):
    browser.find_element_by_xpath('/html/body/section/main/div[5]/div[1]/div[4]/div/div[2]/div/div[2]/div/div[4]/div/div/div/div[3]/div/div[1]/ul[1]/li[1]').click()
    time.sleep(0.5)
    count += 1

browser.quit()




