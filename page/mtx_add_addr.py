'''
document.querySelectorAll('select')
document.querySelectorAll('select')[0]
document.querySelectorAll('select')[0].style
document.querySelectorAll('select')[0].style.display="inline"
document.querySelectorAll('select')[1].style.display="inline"
'''
# 导包
import time

from lesson13.lesson13_1买裙子调用类.base.baseApi import Base
from lesson13.lesson13_1买裙子调用类 import pageObject

from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

# 类中只写动作组合和逻辑组合
class Add_addr(Base):





    # 组合业务
    def add_addr_business(self):
        self.click_mycenter()
        time.sleep(1)
        self.click_myaddr()
        time.sleep(2)
        self.click_addaddr()
        time.sleep(1)
        self.switchto_iframe()
        time.sleep(1)
        self.input_name()
        time.sleep(1)
        self.input_tel()
        time.sleep(1)
        self.select_prov_city_county()
        time.sleep(1)
        self.detail_addr()
        time.sleep(1)
        self.other_name()
        time.sleep(1)
        self.save()

    # 关闭浏览器
    def close_driver(self):
        self.driver.close()

if __name__ =="__main__":

    # 调用登录
    from mtx_login import Login
    from lesson13.lesson13_1买裙子调用类.base.driver import Driver

    driver = Driver().get_driver()

    Login(driver).login_business()

    # 调用新增地址业务
    Add_addr(driver).add_addr_business()
    time.sleep(1)
    assert '新增成功' in driver.page_source

    Driver.close_driver()



