import time
import unittest
import ddt

from lesson13.lesson13_1买裙子调用类.base.baseApi import Base
from lesson13.lesson13_1买裙子调用类 import page

# data = [{'account':'yaoyao', 'pwd':'', 'expect':'密码格式 6~18 个字符之间'},
#     {'account':'', 'pwd':'yaoyao', 'expect':'请填写登录账号'},
#     {'account':'lwx', 'pwd':'yaoyao','expect':'帐号不存在'},
#     {'account':'yaoyao', 'pwd':'123456', 'expect':'密码错误'}]

data = [{'account':'yaoyao', 'pwd':''},
    {'account':'', 'pwd':'yaoyao'},
    {'account':'lwx', 'pwd':'yaoyao'},
    {'account':'yaoyao', 'pwd':'123456'}]

@ddt.ddt
class Mtx_login_ddt(unittest.TestCase,Base):

    # 在首页点击登录按钮
    def click_login_link(self):
        self.base_click(page.loc_login_link)

    @ddt.data(*data)
    def test_input_login(self,test_data):
        # 输入用户名
        # driver.find_element_by_name("accounts").send_keys(test_data['account'])
        print(test_data['account'])
        print(type(test_data['account']))
        self.base_input(page.loc_input_username, test_data['account'])
        time.sleep(3)

        # 输入密码
        # driver.find_element_by_name("pwd").send_keys(test_data['pwd'])
        self.base_input(page.loc_input_pwd, test_data['pwd'])
        time.sleep(3)

        # 点击登录
        # driver.find_element_by_xpath('//form/div[3]/button').click()
        self.base_click(page.loc_click_login)
        time.sleep(3)

        # # 断言
        # # self.assertEqual(driver.page_source, test_data['expect'])
        # assert test_data['expect'] in page_source
        # time.sleep(3)

        # 清空用户名、密码
        # driver.find_element_by_name("accounts").clear()
        self.base_clear(page.loc_input_username)
        time.sleep(3)
        # driver.find_element_by_name("pwd").clear()
        self.base_clear(page.loc_input_pwd)
        time.sleep(3)

if __name__ == '__main__':
    from lesson13.lesson13_1买裙子调用类.base.driver import Driver

    driver = Driver().get_driver()

    unittest.main()
    Mtx_login_ddt(driver).test_input_login()