from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time
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
    mycookies = ('[{"name": "PHPSESSID", "value": "ma95k7oj5t0f5fg7luptql5kv0", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": true, "sameSite": "None"}, {"name": "acf_auth", "value": "0a21fY4EvTrxdmHGFwiWjeZdS9LACFp4RB2LNrzQqPahZQuVpsbICUZLrwv70xWVsv5pMospFXXhrgsFWF%2F159laK%2BlNU7ivoSPVqgzJnBUDbeJQKwT96%2B4", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": true, "expiry": 1616158558, "sameSite": "None"}, {"name": "dy_auth", "value": "9300HtDfM2NaOWY%2BUx%2BrjDZlfJYN7m0IiBRhiCMWfnajFmLJHqQiA8GXZzKXagILUlp3ctDmikMayxyuaQMUR%2FlXhOOGskoayJcwWIuSiMMaarMkP3k3zJk", "path": "/", "domain": ".douyu.com", "secure": false, "httpOnly": true, "expiry": 1616158558, "sameSite": "None"}, {"name": "wan_auth37wan", "value": "30190fc17c67VVDMYoUYNWjEcRp9IJC2ckkQq%2BI7lr%2FZe3jFG7GpNt4s3qf%2BAT2YBiLxU2kF9IGoriWPXwPlY1oO8YhpslzUE8y1CIshO7gZEkwJP8o", "path": "/", "domain": ".douyu.com", "secure": false, "httpOnly": true, "expiry": 1616158558, "sameSite": "None"}, {"name": "acf_uid", "value": "351608479", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": false, "expiry": 1616158558, "sameSite": "None"}, {"name": "acf_username", "value": "351608479", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": false, "expiry": 1616158558, "sameSite": "None"}, {"name": "acf_nickname", "value": "KiRaL1412", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": false, "expiry": 1616158558, "sameSite": "None"}, {"name": "acf_own_room", "value": "0", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": false, "expiry": 1616158558, "sameSite": "None"}, {"name": "acf_groupid", "value": "1", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": false, "expiry": 1616158558, "sameSite": "None"}, {"name": "acf_phonestatus", "value": "1", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": false, "expiry": 1616158558, "sameSite": "None"}, {"name": "acf_avatar", "value": "https%3A%2F%2Fapic.douyucdn.cn%2Fupload%2Favatar_v3%2F202003%2Fbea603ecfea449c1bcb7d86515825c5f_", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": false, "sameSite": "None"}, {"name": "acf_ct", "value": "0", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": false, "expiry": 1616158558, "sameSite": "None"}, {"name": "acf_ltkid", "value": "93792066", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": false, "expiry": 1616158558, "sameSite": "None"}, {"name": "acf_biz", "value": "1", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": false, "expiry": 1616158558, "sameSite": "None"}, {"name": "acf_stk", "value": "4fc8e75345880b09", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": false, "expiry": 1616158558, "sameSite": "None"}, {"name": "dy_did", "value": "bc436103e3ca33c70f13ecdb00061601", "path": "/", "domain": ".douyu.com", "secure": false, "httpOnly": false, "expiry": 1930989358, "sameSite": "None"}, {"name": "acf_did", "value": "bc436103e3ca33c70f13ecdb00061601", "path": "/", "domain": "www.douyu.com", "secure": false, "httpOnly": false, "expiry": 1930989358, "sameSite": "None"}, {"name": "Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7", "value": "1615629345", "path": "/", "domain": ".douyu.com", "secure": false, "httpOnly": false, "expiry": 1647165359, "sameSite": "None"}, {"name": "Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7", "value": "1615629359", "path": "/", "domain": ".douyu.com", "secure": false, "httpOnly": false, "sameSite": "None"}]')

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
