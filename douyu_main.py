from selenium import webdriver
import time
import json 
def browser_initial():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chromedriver = "/usr/bin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=chromedriver)
    browser.get("https://www.douyu.com/2550505")
    browser.maximize_window()
    return browser

def log_csdn(browser):
    #输入你的cookies
    mycookies = ('[{"name": "Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7", "value": "1616314471", "path": "/", "domain": ".douyu.com", "secure": false, "httpOnly": false, "expiry": 1647850471, "sameSite": "None"}, {"name": "Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7", "value": "1616314471", "path": "/", "domain": ".douyu.com", "secure": false, "httpOnly": false, "sameSite": "None"}, {"name": "PHPSESSID", "value": "g8a0nluqo1k31ts4blbs8eo8s2", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": true, "sameSite": "None"}, {"name": "acf_auth", "value": "79e7OCL4t%2B1%2FO3j2%2FXmxqvpeBngUgSohzIWWo82SMI5sUzNcvL75Zjovp2ed6H4D5M2XVbNsntehu9Uz3WnSpMelI84V048VPGAqCD23zgcrd2L7ztwRAdg", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": true, "expiry": 1616843680, "sameSite": "None"}, {"name": "dy_auth", "value": "fc95lOkqjf5Xp5j7BH0UlIp0zafTGFKD8Ew00A%2FpUVjePmc0%2BZshNiEDftiq4DSO7u0IR1eIBScE1SP%2Bj0Sn8fRoiGSNmoNoc4NKpq8nofFFpH13FbnHcMI", "path": "/", "domain": ".douyu.com", "secure": false, "httpOnly": true, "expiry": 1616843680, "sameSite": "None"}, {"name": "wan_auth37wan", "value": "fa773c1fc4caGmrq4%2FqMt1ois5RVvtzpZz20ocbpH8AIQExgCKLn5dEpVhTosfJN%2BYqvy%2BUYM%2FX5PLr5ZU5VoQQKEn0zMVdqFGgkPLhUm6zgUOWjlo0", "path": "/", "domain": ".douyu.com", "secure": false, "httpOnly": true, "expiry": 1616843680, "sameSite": "None"}, {"name": "acf_uid", "value": "351608479", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": false, "expiry": 1616843680, "sameSite": "None"}, {"name": "acf_username", "value": "351608479", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": false, "expiry": 1616843680, "sameSite": "None"}, {"name": "acf_nickname", "value": "KiRaL1412", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": false, "expiry": 1616843680, "sameSite": "None"}, {"name": "acf_own_room", "value": "0", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": false, "expiry": 1616843680, "sameSite": "None"}, {"name": "acf_groupid", "value": "1", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": false, "expiry": 1616843680, "sameSite": "None"}, {"name": "acf_phonestatus", "value": "1", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": false, "expiry": 1616843680, "sameSite": "None"}, {"name": "acf_avatar", "value": "https%3A%2F%2Fapic.douyucdn.cn%2Fupload%2Favatar_v3%2F202003%2Fbea603ecfea449c1bcb7d86515825c5f_", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": false, "sameSite": "None"}, {"name": "acf_ct", "value": "0", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": false, "expiry": 1616843680, "sameSite": "None"}, {"name": "acf_ltkid", "value": "93792067", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": false, "expiry": 1616843680, "sameSite": "None"}, {"name": "acf_biz", "value": "1", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": false, "expiry": 1616843680, "sameSite": "None"}, {"name": "acf_stk", "value": "0e28aaf4a465e0a4", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": false, "expiry": 1616843680, "sameSite": "None"}, {"name": "dy_did", "value": "d9bc7ba32532ec56bf34193f00031601", "path": "/", "domain": ".douyu.com", "secure": false, "httpOnly": false, "expiry": 1931674481, "sameSite": "None"}, {"name": "acf_did", "value": "d9bc7ba32532ec56bf34193f00031601", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": false, "expiry": 1931674481, "sameSite": "None"}]')

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
if(browser.find_element_by_xpath('/html/body/div[7]/span').is_displayed()):
    browser.find_element_by_xpath('/html/body/div[7]/span').click()
bag = browser.find_element_by_xpath('//*[@id="js-player-toolbar"]/div[1]/div[2]/div/div[2]/div/div[4]/div/div/span').click()
time.sleep(5)
while(not(browser.find_element_by_xpath('//*[@id="js-player-toolbar"]/div[1]/div[2]/div/div[2]/div/div[4]/div/div/div/div[3]/div/div[1]/ul[1]/li[1]').is_displayed())):
    browser.find_element_by_xpath('//*[@id="js-player-toolbar"]/div[1]/div[2]/div/div[2]/div/div[4]/div/div/span').click()
time.sleep(5)
#获取礼物数
gift_str = browser.find_element_by_xpath('//*[@id="js-player-toolbar"]/div[1]/div[2]/div/div[2]/div/div[4]/div/div/div/div[3]/div/div[1]/ul[1]/li[1]/span').text
gift_num = int(gift_str)
#点击礼物
count = 0
while(count<gift_num):
    browser.find_element_by_xpath('//*[@id="js-player-toolbar"]/div[1]/div[2]/div/div[2]/div/div[4]/div/div/div/div[3]/div/div[1]/ul[1]/li[1]').click()
    time.sleep(0.5)
    count += 1

time.sleep(5)
browser.quit()
