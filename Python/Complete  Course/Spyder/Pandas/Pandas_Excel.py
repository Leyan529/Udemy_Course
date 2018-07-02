# -*- coding: utf-8 -*-

import pandas as pd

import os
from os import listdir
from os.path import isfile, isdir, join
# 指定要列出所有檔案的目錄
SaveDirectory = os.getcwd() #印出目前工作目錄
# 取得所有檔案與子目錄名稱
files = listdir(SaveDirectory)

GFRIEND_Vedio =""

csvList ={}
print('-------------Read cls File------------')
for f in files:
  fullpath = join(SaveDirectory, f)
  if isdir(fullpath) and f == "ExcelData":       
    excels = listdir(f)
    writePath = fullpath
    for exel in excels: 
        csv={}
        csv["fileName"]= exel
        csv["filePath"]= join(fullpath, exel)
        csvList["GFRIEND_Vedio"] = csv        
#Pandas.read_csv('絕對路徑',
#         names=[新取代的column title list], 
#         header : 以第n個rows為start，將names插入在n的前一個位置)
#         usecols : [] (欲顯示的行數List)  ex : [1,2,3]        
file = pd.read_csv(csvList["GFRIEND_Vedio"]["filePath"])
print(file)
print('---------------------------------------------------')
file = pd.read_csv(csvList["GFRIEND_Vedio"]["filePath"],
                   names=['1','2','3','4'],
                   header=0)
print(file)
print('---------------------------------------------------')
file = pd.read_csv(csvList["GFRIEND_Vedio"]["filePath"],
                   usecols=[0,3])
print(file)
print('-------------Write cls File------------')
file = pd.read_csv(csvList["GFRIEND_Vedio"]["filePath"],                  
                   index_col=False)
print(file)
#Pandas.to_csv('絕對路徑',
#         index : [True : False] 是否寫入索引
file.to_csv(os.path.join(writePath,"GFRIEND_Vedio2.csv"),index=False)
file.to_csv(os.path.join(writePath,"GFRIEND_Vedio2.csv"),index=False)
