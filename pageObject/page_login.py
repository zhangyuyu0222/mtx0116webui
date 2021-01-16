'''
po page object
1,2,3层   1.动作 找到输入框输入   百度一下点击  单独写一个方法：动作的组合   2.动作组合（可有可无）
3.业务层 pytest、unitest 断言  参数化
'''
# 导包

import allure

# 导入Base包，Base包是所有的基础操作方法，如：查找元素、切换窗口、进入iframe等。。。
from lesson13.lesson13_1买裙子调用类.base.baseApi import Base

# 导入pageobject包，导入这个包的目的是，调用__init__文件中的所有元素定位对象
from lesson13.lesson13_1买裙子调用类 import pageObject


# 定义Login类，这个类中只写在登录页面进行的动作。如输入用户名、密码，点击登录。
class PageLogin(Base):

    # 输入用户名
    @allure.step('输入用户名')
    def input_username(self,username):
        # 找到用户名的按钮，点击输入
        self.base_input(pageObject.login_username, username)

    @allure.step('输入密码')
    # 输入密码
    def input_pwd(self,password):
        self.base_input(pageObject.login_pwd, password)

    @allure.step('点击登录')
    # 点击登录
    def click_login(self):
        self.base_click(pageObject.login_button)




















    # # 断言
    # def assert_business(self):
    #     # 页面加载速度较慢，代码运行速度较快，需要让代码等待页面
    #     time.sleep(2)
    #     # if 'yaoyao' in self.driver.page_source:
    #     assert 'yaoyao' in self.driver.page_source
    #     print('yaoyao登录成功')

    # # 组合页面
    # def login_business(self):
    #     # 点击登录链接
    #     self.click_login_link()
    #     # 输入用户名
    #     self.input_username()
    #     # 输入密码
    #     self.input_pwd()
    #     # 点击登录按钮
    #     self.click_login()
    #     # 断言
    #     self.assert_business()
    #     # # 关闭浏览器
    #     # self.close_driver()


