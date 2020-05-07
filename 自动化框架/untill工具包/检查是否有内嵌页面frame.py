from 自动化框架.common.读取文件页名 import read_case
from 自动化框架.common.根据元素进行判断 import do_element
import time

def get_frame(dr,sheetname,num):
    print(f'开始判断是否存在内嵌页面.......')
    fis=read_case().get_lastone(sheetname,num)
    if fis=="":
        do_element(dr,sheetname,num)
    else:
        frame = dr.find_element_by_xpath('//*[@id="main"]/%s' %fis)

        dr.switch_to.frame(frame)  # 切换到指定模块下的内嵌页

        do_element(dr,sheetname,num)

        dr.switch_to.default_content()

if __name__ == '__main__':
  pass