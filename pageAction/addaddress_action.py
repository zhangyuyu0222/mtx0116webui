'''
document.querySelectorAll('select')
document.querySelectorAll('select')[0]
document.querySelectorAll('select')[0].style
document.querySelectorAll('select')[0].style.display="inline"
document.querySelectorAll('select')[1].style.display="inline"
'''
# 导包
import time

# 类中只写动作组合和逻辑组合
from lesson13.lesson13_1买裙子调用类.pageAction.action_manager import ActionManage

class Add_addr(ActionManage):

    # 组合业务
    def add_addr_business(self):
        self.pageindex.click_mycenter()
        time.sleep(1)
        self.pagecenter.click_myaddr()
        time.sleep(2)
        self.pagemyaddr.click_addaddr()
        time.sleep(1)
        self.pagemyaddr.switchto_iframe()
        time.sleep(1)
        self.pagemyaddr.input_name()
        time.sleep(1)
        self.pagemyaddr.input_tel()
        time.sleep(1)
        self.pagemyaddr.select_prov_city_county()
        time.sleep(1)
        self.pagemyaddr.detail_addr()
        time.sleep(1)
        self.pagemyaddr.other_name()
        time.sleep(1)
        self.pagemyaddr.save()





