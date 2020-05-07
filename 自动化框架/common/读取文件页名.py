import os
import xlrd

class read_case():
    """get_filename函数主要是为了获取xlsx文件"""
    def get_filemname(self):
        print(f'我是get_filename')
        files=os.path.abspath("../data存放数据")
        self.filenames=files+"/wu.xlsx"
    """read_file函数主要对xlsx文件进行一个初步的处理"""

    def get_num(self,sheetname):
        print(f'我是get_num')
        self.excel = xlrd.open_workbook("../data存放数据/wu.xlsx")
        print(f'1')

        # 打开文档中的某一个sheet页
        self.sheets = self.excel.sheet_by_name(sheetname)
        # 获取数据行数
        r_num = self.sheets.nrows
        return r_num

    """read_file函数主要是为了对文件内容进行初处理"""
    def read_file(self,sheetname,num):
        print(f'我是read_file')
        # filename=self.filenames
        # 使用xlrd来打开文件
        self.excel = xlrd.open_workbook("../data存放数据/wu.xlsx")

        # 打开文档中的某一个sheet页
        self.sheets = self.excel.sheet_by_name(sheetname)

        # 获取数据行数
        r_num = self.sheets.nrows
        # 读取每一行的数据
        for r in range(num,num+1):
            row_info = self.sheets.row_values(r)
            dats = row_info[5].strip("\n").split(",")
            newlist = []
            for m in dats:
                nc = m.strip("\n")
                newl = nc.split(":")
                newlist.append(newl)
                print(newlist)
            return newlist
    """该get_expect函数主要是为了获取期望结果进行对比"""
    def get_expect(self,sheetname,num):
        print(f'我是get_expect')
        # 使用xlrd来打开文件
        excel = xlrd.open_workbook("../data存放数据/wu.xlsx")
        self.sheetss = excel.sheet_by_name(sheetname)
        # 打开文档中的某一个sheet页
        # 获取数据行数
        for r in range(num, num + 1):
            row_info = self.sheetss.row_values(r)
            return row_info[6]
    def get_lastone(self,sheetname,num):
        excel = xlrd.open_workbook("../data存放数据/wu.xlsx")
        self.sheetss = excel.sheet_by_name(sheetname)
        # 打开文档中的某一个sheet页
        # 获取数据行数
        for r in range(num, num + 1):
            row_info = self.sheetss.row_values(r)
            return row_info[-1]



if __name__ == '__main__':
    get_fid=read_case()