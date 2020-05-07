import time
from selenium.webdriver.support.select import Select
from 自动化框架.common.读取文件页名 import read_case
from 自动化框架.untill工具包.write_log import *


def do_element(dr,sheetname,num):
    # 取出操作进行判断
    print(f'处理事件中........')
    operation = read_case.read_file(dr,sheetname,num)
    for op in operation:
        print(f'op========{op}')
        if op[0] == u"输入":
            print("输入进入")
            ds = do_method(op,dr)
            ds.clear()
            ds.send_keys(op[2])

        elif op[0] == u"点击":
            print("点击进入")
            ds = do_method(op,dr)
            ds.click()

        elif op[0] == u"time":
            time.sleep(1)

        elif op[0] == u"检查":
            check_text=read_case().get_expect(sheetname,num)
            print(f'check_text={check_text}')
            print("检查进入")
            dd = do_method(op,dr).text
            if check_text in dd:
                print("检查成功")
                daytime = time.strftime("%Y-%m-%d-%H:%M:%S")
                write_result().wirte_case(daytime, num,dd,check_text)  #将检查结果写进日志
                # 成功用例进行截图
                check_successful= time.strftime("%Y-%m-%d-%H-%M-%S")
                dr.save_screenshot(r"..\data存放数据\good\%s.png" % check_successful)
            else:
                print("检查失败")
                check_bad = time.strftime("%Y-%m-%d-%H-%M-%S")
                # 失败用例进行截图
                dr.save_screenshot(r"..\data\bad\%s.png" % check_bad)
                daytimes = time.strftime("%Y-%m-%d-%H:%M:%S")
                write_result().write_badcase(daytimes,num,dd,check_text)  # 将检查结果写进日志

        elif op[0] == u"选择":
            ds = do_method(op,dr)
            ds.select_by_visible_text(op[2])

        elif op[0] == u"刷新":
            dr.refresh()

def do_method(op,dr):
    print("元素查找中.......")
    print(f"op=={op}")
    do_new = op[1].split("==")
    time.sleep(1)
    try:
        if do_new[0] == "xpath":
            print(f'这个xpath={do_new[1]}')
            return dr.find_element_by_xpath(do_new[1])
        elif do_new[0] == "id":
            print(f'这个id={do_new[1]}')
            return dr.find_element_by_id(do_new[1])
        elif do_new[0] == "link":
            print(f'这个link={do_new[1]}')
            return dr.find_elements_by_partial_link_text(do_new[1])
        elif do_new[0] == "select":
            print(f'这个select={do_new[1]}')
            return Select(dr.find_element_by_xpath(do_new[1]))
        elif do_new[0 ]== "name":
            print(f'这个name={do_new[1]}')
            return dr.find_element_by_name(do_new[1])
    except:
        print(f'元素流产')

if __name__ == '__main__':
    pass