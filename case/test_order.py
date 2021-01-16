import time

import allure

from lesson13.lesson13_1买裙子调用类.base.baseApi import Base
from lesson13.lesson13_1买裙子调用类.base.driver import Driver
from lesson13.lesson13_1买裙子调用类.pageAction.login_action import Login
from lesson13.lesson13_1买裙子调用类.pageAction.order_action import Buy_pinkskirt

@allure.feature('下订单测试')
class TestOrder():
    def setup_class(self):
        #创建driver对象
        self.driver = Driver.get_driver()

        # 依赖登录，调用成功登录的业务
        Login(self.driver).login_success()
        # 实例化base对象
        self.base = Base(self.driver)
        # 创建order对象
        self.order = Buy_pinkskirt(self.driver)

    @allure.title('下订单的测试用例')
    def test_order(self):
        #调用下订单业务
        self.order.buy_pinkskirt_business()
        time.sleep(3)
        assert '提交成功' in self.base.base_page_source

    # 关闭driver
    def teardown_class(self):
        Driver.close_driver()


