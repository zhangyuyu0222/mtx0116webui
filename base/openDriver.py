from selenium import webdriver


class OpenDriver:
    def get_driver(self,browser):
        '''
        对具体哪一个浏览器的封装
        :param browser: 浏览器的名字：ie，firefox，chrome
        :return: 指定浏览器的driver对象
        '''
        if browser == 'firefox' or browser == 'ff':
            driver = webdriver.Firefox()
            return driver

        elif browser == 'chrome' or browser == '谷歌':
            driver = webdriver.Chrome()
            return driver

        elif browser == 'ie' or browser == 'internet':
            driver = webdriver.Ie()
            return driver

        else:
            raise NameError('Not found{}browser,please check browser name'.format(browser))

if __name__=='__main__':
    OpenDriver().get_driver('谷歌')