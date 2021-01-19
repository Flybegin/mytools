"""
for PDF file splite

by snial 2021/01/18
"""

import sys
import os
from PyPDF2 import PdfFileReader,PdfFileWriter

def shuzhu(path,name,nums): #使用分割点页码进行分割
    for j in range(0,len(nums)-1,1):
        begin = int(nums[j])-1
        end = int(nums[j+1])-1
        splite(path,name,begin,end)


def configs(path,name,nums): #使用配置文件进行分割
    for num in nums:
        begin = int(num.split('-')[0])-1
        end = int(num.split('-')[1])
        if begin > end:
            z = begin
            begin = end
            end = z
        splite(path,name,begin,end)

def split_arv(path,name,num):  #使用固定页数进行分割
    long = path.getNumPages()
    for i in range(0,long,num):
        bengin = i
        end = i+num
        if end > long:
            end = long
        splite(path,name,bengin,end)


def splite(path,name,begin,end):#分割函数
    pdf_writer = PdfFileWriter()
    print("程序开始分割{}到{}".format(begin+1, end))
    output = f'./{name}/{name}-{begin+1}-{end}.pdf'
    for i in range(int(begin), int(end)):
        page1 = path.getPage(i)
        pdf_writer.addPage(page1)
    with open(output, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)
    print("程序分割完成{}到{}".format(begin+1, end))



if __name__=='__main__':
    filename = sys.argv[1]
#    filename = 'text.pdf'
    named=filename.split('.')[0]
    os.mkdir(named)
    read = open(filename,'rb')
    pdffile = PdfFileReader(read)

    if sys.argv[2] == '-f' :  # 使用配置文件configs 进行分割
        config = sys.argv[3]
        split_nums = []
        with open(config, 'r') as config_txt:
            text_split = config_txt.readlines()
            for text in text_split:
                text=text.strip()
                split_nums.append(text)
        print("准备开始使用配置文件进行分割")
        configs(pdffile, named, split_nums)

    elif sys.argv[2] == '-i':  #使用固定间距进行分割
        split_num = sys.argv[3]
        print("准备开始使用固定间距进行分割")
        split_arv(pdffile, named, int(split_num))

    elif sys.argv[2] == '-s':
        split_nums = []
        txt = sys.argv[3]
        txt_num = txt.split(',')
        print("准备开始使用分割点进行分割")
        shuzhu(pdffile,named,txt_num)

    else:
        print("===========PDF_splite===========")
        print("请输入合适得参数")
        print("-f filename  使用配置文件进行分割")
        print("-i num       使用固定间距进行分割")
        print("-s n1,n2,n3  使用分割点进行分割")
        print("==========by_liushui============")
    read.close()

