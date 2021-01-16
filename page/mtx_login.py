'''
po page object
1,2,3层   1.动作 找到输入框输入   百度一下点击  单独写一个方法：动作的组合   2.动作组合（可有可无）
3.业务层 pytest、unitest 断言  参数化
'''
# 导包
import time

from lesson13.lesson13_1买裙子调用类.base.baseApi import Base
from lesson13.lesson13_1买裙子调用类 import page

# 类中只写动作（定位元素，对元素进行操作）组合和逻辑组合
class Login(Base):

    # 页面动作
    # 在首页点击登录按钮
    def click_login_link(self):
        self.base_click(page.loc_login_link)
    # 输入用户名
    def input_username(self):
        # 找到用户名的按钮，点击输入
        self.base_input(page.loc_input_username, 'yaoyao')
    # 输入密码
    def input_pwd(self):
        self.base_input(page.loc_input_pwd, 'yaoyao')
    # 点击登录
    def click_login(self):
        self.base_click(page.loc_click_login)

    # 断言
    def assert_business(self):
        # 页面加载速度较慢，代码运行速度较快，需要让代码等待页面
        time.sleep(2)
        # if 'yaoyao' in self.driver.page_source:
        assert 'yaoyao' in self.driver.page_source
        print('yaoyao登录成功')

    # 组合页面
    def login_business(self):
        # 点击登录链接
        self.click_login_link()
        # 输入用户名
        self.input_username()
        # 输入密码
        self.input_pwd()
        # 点击登录按钮
        self.click_login()
        # 断言
        self.assert_business()
        # # 关闭浏览器
        # self.close_driver()


if __name__ =="__main__":
    from lesson13.lesson13_1买裙子调用类.base.driver import Driver

    driver = Driver().get_driver()

    login = Login(driver)
    # 成功登录的方法：
    login.login_business()
