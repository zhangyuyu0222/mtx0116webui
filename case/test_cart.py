import time

import allure

from lesson13.lesson13_1买裙子调用类.base.baseApi import Base
from lesson13.lesson13_1买裙子调用类.base.driver import Driver
from lesson13.lesson13_1买裙子调用类.pageAction.login_action import Login
from lesson13.lesson13_1买裙子调用类.pageAction.cart_action import Cart

'''
case
测试用例（N）
1.起始动作是在哪个页面---
原则：1.保证起始动作在相同的页面
    2.目的：回到首页
    2.1 前一个测试用例结束的时候，点击“首页”按钮----进入首页，接着执行后一个测试用例
    todo: 销毁函数 teardown_method()
    2.2 在后一个测试用例开始前，get（首页url）
    todo: 初始化函数：setup_method()
'''

@allure.feature('删除购物车测试')
class TestCart():

    def setup_class(self):
        #创建driver对象
        self.driver = Driver.get_driver()

        # 依赖登录，调用成功登录的业务
        Login(self.driver).login_success()
        # 实例化base对象
        self.base = Base(self.driver)
        # 创建cart对象
        self.cart = Cart(self.driver)

    # 关闭driver
    def teardown_class(self):
        Driver.close_driver()

    # #销毁函数，点击index首页
    # def teatdown_method(self):
    #     self.base.base_click_index()

    # 第二种方法
    def setup_method(self):
        self.driver.get('http://121.42.15.146:9090/mtx/')

    @allure.title('加入购物车的测试用例')
    def test_addtocart(self):
        self.cart.addto_cart_business()
        time.sleep(3)
        assert '加入成功' in self.base.base_page_source


    @allure.title('删除购物车的测试用例')
    def test_detelecart(self):
        #调用删除购物车业务
        self.cart.delete_cart_business()
        time.sleep(3)
        assert '删除成功' in self.base.base_page_source




