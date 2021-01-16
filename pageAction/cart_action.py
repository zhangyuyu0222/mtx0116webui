# 导包
import time

from lesson13.lesson13_1买裙子调用类.pageAction.action_manager import ActionManage

'''
组合业务
引入页面对象
'''

class Cart(ActionManage):

    def addto_cart_business(self):
        self.pageindex.click_pinkskirt()
        time.sleep(1)
        self.pageindex.change_window()
        time.sleep(1)
        self.pagegoogsdetail.click_pink()
        time.sleep(1)
        self.pagegoogsdetail.click_M()
        time.sleep(1)
        self.pagegoogsdetail.click_addto_cart()
        time.sleep(1)


    # 组合业务：删除购物车
    def delete_cart_business(self):
        '''
        功能测试，手动如何测试，自动化动作就如何操作
        删除商品之前要确保购物车里有商品
        （推荐）1.action层，先调用添加购物车业务（确保购物车里有商品），再调用删除业务
        1.1 动作能关联上。
        2.case层，调整顺序，插件pytest-ordering(不推荐使用：要保证测试用例之间是相互独立的)，order=1（）
        :return:
        '''
        self.addto_cart_business()
        time.sleep(3)

        self.pagegoogsdetail.click_goodsdetail_cart()
        time.sleep(1)

        self.pagecart.click_delete()
        time.sleep(1)
        self.pagecart.click_delete_ok()
        time.sleep(1)

    # 点击首页
    def click_index(self):
        pass





