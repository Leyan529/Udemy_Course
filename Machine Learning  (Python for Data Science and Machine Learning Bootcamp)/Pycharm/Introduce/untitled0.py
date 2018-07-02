# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 16:23:34 2017

@author: Leyan
"""

#這行是在ipython notebook的介面裏專用，如果在其他介面則可以拿掉
#%matplotlib inline
from sklearn import datasets

import matplotlib.pyplot as plt

#載入數字資料集
digits = datasets.load_digits()

#畫出第一個圖片
plt.figure(1, figsize=(3, 3))
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()