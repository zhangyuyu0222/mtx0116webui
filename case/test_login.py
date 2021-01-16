import time

import allure
import pytest

from lesson13.lesson13_1买裙子调用类.base.driver import Driver
from lesson13.lesson13_1买裙子调用类.pageAction.login_action import Login
from lesson13.lesson13_1买裙子调用类.tool.readData import ReadData
from lesson13.lesson13_1买裙子调用类.base.baseApi import Base
data = ReadData().get_yaml('login_data','test_login')

'''
登录用例的参数化数据如何组织？如何断言？
1.前面是登录失败的，后一条是登陆成功的
2.没有顺序，随便写
2.1 判断：如果成功了，先退出。判断是否退出成功，退出成功在继续参数化。
前提条件：类级别的装置函数（setup_class,teardown_class)
2.2 前提条件：装置函数可以用方法级别的
'''
@allure.feature('登录测试')
class TestLogin:

    def setup_class(self):
        '''
        初始化chrome对象
        :return:
        '''
        # 创建driver对象
        self.driver = Driver.get_driver()
        # 创建login的业务对象
        self.login = Login(self.driver)
        # 创建base对象，调用page_source的方法
        self.base = Base(self.driver)

    @pytest.mark.parametrize('args',data)
    def test_login(self,args):
        self.login.login_business(args['accounts'], args['pwd'])
        time.sleep(2)
        assert args['assert'] in self.base.base_page_source

    def teardown_class(self):
        '''
        所有测试用例执行完成关闭浏览器
        :return:
        '''

        Driver.close_driver()