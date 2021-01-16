import allure

# 导入Base包，Base包是所有的基础操作方法，如：查找元素、切换窗口、进入iframe等。。。
from lesson13.lesson13_1买裙子调用类.base.baseApi import Base

# 导入pageobject包，导入这个包的目的是，调用__init__文件中的所有元素定位对象
from lesson13.lesson13_1买裙子调用类 import pageObject


# 定义Login类，这个类中只写在登录页面进行的动作。如输入用户名、密码，点击登录。
class PageCart(Base):

    # 点击删除按钮
    @allure.step('点击删除按钮')
    def click_delete(self):
        self.base_click(pageObject.delete_click_delete)

    # 点击确定按钮
    @allure.step('点击确定按钮')
    def click_delete_ok(self):
        self.base_click(pageObject.delete_click_ok)