from selenium.webdriver.common.by import By
'''
整个项目的配置项
'''
# url地址
url = 'http://121.42.15.146:9090/mtx/'

# 返回首页
index_title = '码同学实战系统'

# 登录参数
login_link = By.LINK_TEXT, "登录"
login_username = By.NAME, "accounts"
login_pwd = By.NAME, "pwd"
login_button = By.XPATH, '//form/div[3]/button'

# 下单功能的配置
loc_pinkskirt = By.CSS_SELECTOR,'#floor2 div.goods-list>div:nth-child(1)'
title_ZK = "ZK爆款连衣裙"
loc_pink = By.XPATH, '//*[@data-value="粉色"]'
loc_M = By.XPATH, '//*[@data-value="M"]'
loc_buy_now = By.XPATH, '//*[text()="立即购买"]'
loc_addto_cart = By.XPATH, '//*[text()="加入购物车"]'
loc_givemoney = By.XPATH, '//*[text()="货到付款"]'
loc_submit = By.XPATH, '//*[text()="提交订单"]'

# 新增地址的配置
loc_mycenter = By.XPATH, '//*[text()="个人中心"]'
loc_myaddr = By.LINK_TEXT, '我的地址'
loc_addaddr = By.XPATH, '//button[@data-popup-title="新增地址"]'
loc_input_name = By.NAME, 'name'
loc_input_tel = By.NAME, 'tel'
loc_detail_addr = By.NAME, 'address'
loc_other_name = By.NAME, 'alias'
loc_save = By.XPATH, '//*[text()="保存"]'
loc_prov = By.NAME, 'province'
loc_city = By.NAME, 'city'
loc_county = By.NAME, 'county'
js_prov = "document.querySelectorAll('select')[0].style.display='inline'"
js_city = "document.querySelectorAll('select')[1].style.display='inline'"
js_county = "document.querySelectorAll('select')[2].style.display='inline'"


# 购物车页面
index_click_right_cart = By.XPATH,'(//*[text()="购物车"])'
delete_click_delete = By.XPATH, '(//*[text()="删除"])[1]'
delete_click_ok = By.XPATH, '//*[text()="确定"]'
index_click_ = By.CSS_SELECTOR, 'div#doc-topbar-collapse>ul>li:nth-child(1)>a'


