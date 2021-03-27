from selenium import webdriver
from time import sleep
import json
if __name__ == '__main__':
    option = webdriver.FirefoxOptions()
    option.add_argument('headless')
    driver = webdriver.Firefox(options=option)
    driver.maximize_window()
    driver.get('https://www.douyu.com/')
    sleep(6)
    # driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="anony-reg-new"]/div/div[1]/iframe'))  # 切换浏览器标签定位的作用域

    webdriver.ActionChains(driver).move_to_element(driver.find_element_by_xpath('/html/body/div[1]/header/div/div/div/div[3]/div[7]/div/div/a/span')).click(driver.find_element_by_xpath('/html/body/div[1]/header/div/div/div/div[3]/div[7]/div/div/div/div/div/div[2]/a[1]')).perform()
    

    sleep(10)
    dictCookies = driver.get_cookies()  # 获取list的cookies
    jsonCookies = json.dumps(dictCookies)  # 转换成字符串保存
    with open('mycookies.txt', 'w') as f:
        f.write(jsonCookies)
    print('cookies保存成功！')
