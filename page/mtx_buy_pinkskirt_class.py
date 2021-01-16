# 导包
import time
from lesson13.lesson13_1买裙子调用类 import page

from selenium.webdriver.common.by import By

from lesson13.lesson13_1买裙子调用类.base.baseApi import Base

class Buy_pinkskirt(Base):



    def buy_pinkskirt_business(self):
        self.click_pinkskirt()
        time.sleep(1)
        self.change_window()
        time.sleep(1)
        self.click_pink()
        time.sleep(1)
        self.click_M()
        time.sleep(1)
        self.click_buy_now()
        time.sleep(1)
        self.click_givemoney()
        time.sleep(1)
        self.submit()


if __name__ =="__main__":
    # 调用登录
    from mtx_login import Login
    from lesson13.lesson13_1买裙子调用类.base.driver import Driver

    driver = Driver().get_driver()

    Login(driver).login_business()

    Buy_pinkskirt(driver).buy_pinkskirt_business()
    time.sleep(2)

    assert '提交成功' in driver.page_source

    Driver.close_driver()

    # By.ID等同于 find_element_by_id
    driver.find_element(By.ID,)


