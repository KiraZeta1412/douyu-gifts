from selenium import webdriver
import time
import json 
import os
def browser_initial():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chromedriver = "/usr/bin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    browser = webdriver.Chrome(options=chrome_options,executable_path=chromedriver)
    browser.get("https://www.douyu.com/2550505")
    browser.maximize_window()
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
browser.implicitly_wait(30)
#点击背包
if(browser.find_element_by_css_selector('.SuperFansGuideTips-close').is_displayed()):
    browser.find_element_by_css_selector('.SuperFansGuideTips-close').click()
browser.implicitly_wait(30)
time.sleep(5)
bag = browser.find_element_by_css_selector('.PlayerToolbar-backpackArea').click()
browser.implicitly_wait(30)
time.sleep(2)
browser.refresh()
browser.find_element_by_css_selector('.PlayerToolbar-backpackArea').click()
browser.implicitly_wait(30)

time.sleep(5)
#获取礼物数
gift_str = browser.find_element_by_css_selector('.Backpack-propCount').text
gift_num = int(gift_str)
#点击礼物
count = 0
while(count<gift_num):
    browser.find_element_by_css_selector('#js-player-toolbar > div > div:nth-child(2) > div > div.PlayerToolbar-ContentCell.is-full > div > div.PlayerToolbar-backpackArea > div > div > div > div:nth-child(3) > div > div.Backpack-propWrap > ul:nth-child(1) > li.Backpack-prop.prop.is-effect').click()
    time.sleep(0.5)
    count += 1

time.sleep(5)
browser.quit()
