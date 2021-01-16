# 导包
import time

from lesson13.lesson13_1买裙子调用类.pageAction.action_manager import ActionManage

'''
组合业务
引入页面对象
'''

class Buy_pinkskirt(ActionManage):

    def buy_pinkskirt_business(self):
        self.pageindex.click_pinkskirt()
        time.sleep(1)
        self.pageindex.change_window()
        time.sleep(1)
        self.pagegoogsdetail.click_pink()
        time.sleep(1)
        self.pagegoogsdetail.click_M()
        time.sleep(1)
        self.pagegoogsdetail.click_buy_now()
        time.sleep(1)
        self.pagebuy.click_givemoney()
        time.sleep(1)
        self.pagebuy.submit()




