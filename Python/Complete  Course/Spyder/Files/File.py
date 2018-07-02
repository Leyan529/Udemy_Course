# -*- coding: utf-8 -*-

from os import listdir
from os.path import isfile, isdir, join

# 指定要列出所有檔案的目錄
SaveDirectory = os.getcwd() #印出目前工作目錄

# 取得所有檔案與子目錄名稱
files = listdir(SaveDirectory)

# 以迴圈處理
for f in files:
  # 產生檔案的絕對路徑
  fullpath = join(SaveDirectory, f)
  # 判斷 fullpath 是檔案還是目錄
  if isfile(fullpath):
    print("檔案：", f)
  elif isdir(fullpath):
    print("目錄：", f)
