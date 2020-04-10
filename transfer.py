# -*- coding: utf-8 -*-
import os, shutil, sys

################################################################################
# 程序日志记录
class Logger(object):
    def __init__(self, filename='default.log', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'w')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


sys.stdout = Logger('.\\程序输出日志.log', sys.stdout)
sys.stderr = Logger('.\\程序Bug日志.log_file', sys.stderr)
##############################################
# 如果【井】目录存在则删除
isExists = os.path.exists('.\\【井】')
if isExists:
    shutil.rmtree('.\\【井】')

isExists = os.path.exists('.\\【分类】')
if isExists:
    shutil.rmtree('.\\【分类】')
#############################################
# 索引原始文件名
PATH_ORI = ".\\ORI\\"
fileNameSet_ORI = []
for fileName in os.listdir(PATH_ORI):
    # print(fileName)
    # if 'ORI' in fileName:
    fileNameSet_ORI.append(fileName)
# print(fileNameSet_ORI)  # 原始文件名组成的list

#############################################
# 开始地毯式搜索
PATH = ".\\"
fileNameSet = []
# for fileName in os.listdir(PATH):
#     if '#' in fileName and 'GC' in fileName:
#         fileNameSet.append(fileName)
for root, dirs, files in os.walk(PATH):
    # for fileName in files:
    #     if '#' in fileName and 'GC' in fileName:
    #         fileNameSet.append(fileName)
    # 搜索所有的目录
    for fileName in dirs:
        if '#' in fileName and 'GC' in fileName:
            if '201910' in fileName or '201911' in fileName or '201912' in fileName or '202001' in fileName \
                    or '202002' in fileName or '202003' in fileName or '202004' in fileName:
                fileNameSet.append(fileName)
# print(fileNameSet)  # 要查找的井组成的list

############################################
# 创建【井】文件夹
for item_Full_Name in fileNameSet:
    # print(item_Full_Name)
    os.makedirs('.\\【井】\\' + item_Full_Name + '\\yssj')

############################################
# 愚公移山
for item_Full_Name in fileNameSet:
    item = item_Full_Name.split('#')[0]
    # print('watch' + item)
    for item_ORI in fileNameSet_ORI:
        # print(item_ORI)
        if item in item_ORI:
            shutil.copy(PATH_ORI + item_ORI, '.\\【井】\\' + item_Full_Name + '\\yssj')

############################################
# 垃圾分类
PATH = ".\\【井】\\"
os.makedirs('.\\【分类】\\0个原始文件的')
os.makedirs('.\\【分类】\\1个原始文件的')
os.makedirs('.\\【分类】\\2个原始文件的')
os.makedirs('.\\【分类】\\3个原始文件的')
os.makedirs('.\\【分类】\\4个原始文件的')
os.makedirs('.\\【分类】\\5个以上原始文件的')
item_Full_Name0 = []
item_Full_Name1 = []
item_Full_Name2 = []
item_Full_Name3 = []
item_Full_Name4 = []
item_Full_NameX = []
for item_Full_Name in fileNameSet:
    count = 0
    for root, dirs, files in os.walk(PATH + item_Full_Name + '\\yssj'):  # 遍历统计
        for each in files:
            count += 1
    if count == 0:
        item_Full_Name0.append(item_Full_Name)
        shutil.move(PATH + item_Full_Name, '.\\【分类】\\0个原始文件的')
    if count == 1:
        item_Full_Name1.append(item_Full_Name)
        shutil.move(PATH + item_Full_Name, '.\\【分类】\\1个原始文件的')
    if count == 2:
        item_Full_Name2.append(item_Full_Name)
        shutil.move(PATH + item_Full_Name, '.\\【分类】\\2个原始文件的')
    if count == 3:
        item_Full_Name3.append(item_Full_Name)
        shutil.move(PATH + item_Full_Name, '.\\【分类】\\3个原始文件的')
    if count == 4:
        item_Full_Name4.append(item_Full_Name)
        shutil.move(PATH + item_Full_Name, '.\\【分类】\\4个原始文件的')
    if count > 4:
        item_Full_NameX.append(item_Full_Name)
        shutil.move(PATH + item_Full_Name, '.\\【分类】\\5个以上原始文件的')

# 如果【井】目录存在则删除
isExists = os.path.exists('.\\【井】')
if isExists:
    shutil.rmtree('.\\【井】')

print('0个原始文件的：', item_Full_Name0)
print('\n1个原始文件的：', item_Full_Name1)
print('\n2个原始文件的：', item_Full_Name2)
print('\n3个原始文件的：', item_Full_Name3)
print('\n4个原始文件的：', item_Full_Name4)
print('\n5个以上原始文件的：', item_Full_NameX)
input()