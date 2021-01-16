from selenium.webdriver.common.by import By
'''
整个项目的配置项
'''
# url地址
url = 'http://121.42.15.146:9090/mtx/'

# 登录参数
loc_login_link = By.LINK_TEXT, "登录"
loc_input_username = By.NAME, "accounts"
loc_input_pwd = By.NAME, "pwd"
loc_click_login = By.XPATH, '//form/div[3]/button'

# 下单功能的配置
loc_pinkskirt = By.CSS_SELECTOR,'#floor2 div.goods-list>div:nth-child(1)'
title_ZK = "ZK爆款连衣裙"
loc_pink = By.XPATH, '//*[@data-value="粉色"]'
loc_M = By.XPATH, '//*[@data-value="M"]'
loc_buy_now = By.XPATH, '//*[text()="立即购买"]'
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
js_prov = "document.querySelectorAll('select')[0].style.display='inline'"
js_city = "document.querySelectorAll('select')[1].style.display='inline'"
js_county = "document.querySelectorAll('select')[2].style.display='inline'"
