from selenium import webdriver
import time
from 自动化框架.common.根据元素进行判断 import do_element
from 自动化框架.untill工具包.检查是否有内嵌页面frame import get_frame

#"""login_dr函数主要是为了得到一个窗口便于后面的用例在一个窗口，避免重复打开"""

class login():
    def login_dr(self):
        print(f'我是登录')
        self.dr=webdriver.Chrome()
        self.dr.implicitly_wait(10)
        self.dr.get("http://wukong.icl-network.com/admin")
        self.dr.maximize_window()
        self.dr.find_element_by_id("username").send_keys("18284027997")
        self.dr.find_element_by_id("password").send_keys("admin")
        self.dr.find_element_by_xpath('//*[@id="loginForm"]/div[1]/input').click()
        return self.dr

    """用例执行完后关闭窗口"""
    def login_close(self):
        self.dr.close()

if __name__ == '__main__':
    login().login_dr()