from lesson13.lesson13_1买裙子调用类.pageObject.page_buy import PageBuy
from lesson13.lesson13_1买裙子调用类.pageObject.page_center import PageCenter
from lesson13.lesson13_1买裙子调用类.pageObject.page_goods_detail import PageGoodsDetail
from lesson13.lesson13_1买裙子调用类.pageObject.page_index import PageIndex
from lesson13.lesson13_1买裙子调用类.pageObject.page_login import PageLogin
from lesson13.lesson13_1买裙子调用类.pageObject.page_myaddr import PageMyAddr
from lesson13.lesson13_1买裙子调用类.pageObject.page_cart import PageCart


class ActionManage:
    '''
    管理页面对象的
    有多少个页面对象，就实例化多少对象，
    '''
    def __init__(self,driver):
        self.pagelogin = PageLogin(driver)
        self.pageindex = PageIndex(driver)
        self.pagegoogsdetail = PageGoodsDetail(driver)
        self.pagebuy = PageBuy(driver)
        self.pagecenter = PageCenter(driver)
        self.pagemyaddr = PageMyAddr(driver)
        self.pagecart = PageCart(driver)