'''
po page object
1,2,3层   1.动作 找到输入框输入   百度一下点击  单独写一个方法：动作的组合   2.动作组合（可有可无）
3.业务层 pytest、unitest 断言  参数化
'''
# 导包


import allure
# 导入Base包，Base包中写的是所有常用方法的定义，如查找元素，切换窗口，进入iframe等
from lesson13.lesson13_1买裙子调用类.base.baseApi import Base
# 导入pageObject包，目的是要调用__init__文件中定义的所有定位元素的对象
from lesson13.lesson13_1买裙子调用类 import pageObject

# 定义首页类，类中只写在首页进行的动作，如点击登录按钮，点击我的中心按钮，点击商品等。。。
class PageIndex(Base):

    # 页面动作
    # 在首页点击登录按钮
    @allure.step('在首页点击登录按钮')
    def click_login_link(self):
        self.base_click(pageObject.login_link)

    @allure.step('在首页点击ZK裙子')
    def click_pinkskirt(self):
        self.base_click(pageObject.loc_pinkskirt)

    #切换窗口（过渡动作，前移---写在触发这个动作的页面上）
    @allure.step('切换窗口的方法，要写在触发这个动作的页面内，即首页界面')
    def change_window(self):
        self.base_switch_window(pageObject.title_ZK)

    # 点击个人中心
    @allure.step('在首页点击个人中心按钮')
    def click_mycenter(self):
        self.base_click(pageObject.loc_mycenter)

    # # 点击右上角的购物车
    # @allure.step('在首页点击购物车按钮')
    # def click_right_cart(self):
    #     self.base_click(pageObject.index_click_right_cart)

