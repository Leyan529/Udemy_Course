# -*- coding: utf-8 -*-
import numpy as np

#array
#numpy.arrange(min,max,modify) -> 效果同for-loop => 產生一個由min到max-1的list
dArr1 = np.arange(0,21,5) #1-d
print("1-d:")
print(dArr1)

#numpy.arrange(min,max,modify).reshape(d-menx,d-meny,d-menz)
dArr2 = np.arange(0,96,16).reshape(3,2) #2-d
print("2-d:")
print(dArr2)

dArr3 = np.arange(0,96,4).reshape(3,2,4) #3-d
print("3-d:")
print(dArr3)

#numpy.ones(size, dtype=None, order='C')
onesA = np.ones(10)
print(onesA)
print(onesA.size)

onesA = np.ones(5,dtype= np.int)
print(onesA)
print(onesA.size)