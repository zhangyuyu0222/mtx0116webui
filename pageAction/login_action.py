import time
from lesson13.lesson13_1买裙子调用类.pageAction.action_manager import ActionManage

'''
方法一：
在登录这个类中进行两个页面的实例化

方法二：
多继承！
'''


class Login(ActionManage):
    '''
    组合业务
    1.登录业务需要哪几个页面的哪几个步骤
    2.登录页面   3个步骤
    3.index页面  1个步骤

    '''


    # 组合业务：登录成功的业务
    def login_success(self):
        # 点击首页的登录链接
        self.pageindex.click_login_link()
        # 输入用户名
        self.pagelogin.input_username('yaoyao')
        # 输入密码
        self.pagelogin.input_pwd('yaoyao')
        # 点击登录
        self.pagelogin.click_login()
        time.sleep(3)


    # 组合业务：登录业务（参数化）
    def login_business(self,username,password):
        # 点击首页的登录链接
        self.pageindex.click_login_link()
        # 输入用户名
        self.pagelogin.input_username(username)
        # 输入密码
        self.pagelogin.input_pwd(password)
        # 点击登录
        self.pagelogin.click_login()
        time.sleep(3)


'''
方法二
'''
# class Login(PageLogin,PageIndex):
#     '''
#     组合业务
#     1.登录业务需要哪几个页面的哪几个步骤
#     2.登录页面   3个步骤
#     3.index页面  1个步骤
#
#     '''
#
#     # 组合业务：登录成功的业务
#     def login_success(self):
#         # 点击首页的登录链接
#         self.click_login_link()
#         # 输入用户名
#         self.input_username('yaoyao')
#         # 输入密码
#         self.input_pwd('yaoyao')
#         # 点击登录
#         self.click_login()
#
#     # 组合业务：登录业务（参数化）
#     def login_business(self, username, password):
#         # 点击首页的登录链接
#         self.click_login_link()
#         # 输入用户名
#         self.input_username(username)
#         # 输入密码
#         self.input_pwd(password)
#         # 点击登录
#         self.click_login()

