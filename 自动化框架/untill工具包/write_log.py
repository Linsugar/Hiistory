
"""这个函数主要是为了对每一条用例进行截图-计数-说明进行的记录"""

class write_result():
    def wirte_case(self,daytime, num, dd, check_text):
        ls = "在%s时间段第%s条用例-成功-实际结果:%s,预期结果:%s" % (daytime, num, dd, check_text)
        with open("../log/logs.txt",mode='a')as fie:
            fie.write(ls +'\n')
    def write_badcase(self,daytime, num, dd, check_text):
        ls = "在%s时间段第%s条用例-失败-实际结果:%s,预期结果:%s" % (daytime, num, dd, check_text)
        with open("../log/logs.txt", mode='a')as fie:
            fie.write(ls + '\n')