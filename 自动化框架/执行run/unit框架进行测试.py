from 自动化框架.common.读取文件页名 import *
import unittest
import time
from 自动化框架.common.HTMLTestRunner import HTMLTestRunner
from 自动化框架.common.业务登录关闭模块 import login
from 自动化框架.untill工具包.检查是否有内嵌页面frame import get_frame

class UI_runer(unittest.TestCase):

    """test_work主要执行工作台页面的用例"""
    @classmethod
    def setUpClass(cls):
        cls.drs=login().login_dr()

    def test_wrok(self):

        getnumber=read_case()
        num=getnumber.get_num("wu")
        for i in range(1,num):
            print(f'i={i}')
            get_frame(self.drs,"wu",i)

    """test_magen主要执行配置管理模块的用例"""
    # def test_magen(self):
    #     pass
    # """test_customer主要执行客户管理模块的用例"""
    # def test_customer(self):
    #     pass
    # @classmethod
    # def tearDownClass(cls):
    #     pass




if __name__ == '__main__':
    # 定义脚本标题，加u是支持utf8
    report_title = u'模块测试报告：'

    # 定义详情内容
    desc = u'模块测试报告详情：'

    # 定义一个日期时间戳
    date = time.strftime('%Y%m%d')
    time = time.strftime('%Y%m%d%H%M%S')

    path = '../生成报告report/'+ time + '/'
    # 判断是否定义的路径目录存在，不能存在则创建

    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass

    report_path = path + 'report.html'

    # 定义一个测试容器
    suite = unittest.TestSuite()  # 初始化一个测试套
    loader = unittest.TestLoader()  # 初始化用例加载
    suite.addTests(loader.loadTestsFromTestCase(UI_runer))
    # 将运行结果保存到report，名字为定义的路径和文件名，运行脚本

    with open(report_path, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(suite)
    # 关闭report，脚本结束
    report.close()