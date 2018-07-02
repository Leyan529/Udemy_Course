# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d #3D繪圖套件
import numpy as np
import random

fig = plt.figure()


chart = fig.add_subplot(1,1,1, projection = '3d')

x=[]    #X座標
y=[]    #Y座標
z=[]    #Z座標

weight_x = np.ones(10) #X座標權重
#weight_y = np.ones(10) #Y座標權重
weight_y = []
weight_z = []          #Z座標權重

for i in range(1,11,1):    
    x.append(i)
    y.append(i)
    z.append(0)
    
    weight_y.append(1)
    weight_z.append(i) 
    

chart.bar3d(x,y,z,weight_x,weight_y,weight_z,color = 'g')



chart.set_xlabel('x_label')
chart.set_ylabel('y_label')
chart.set_zlabel('z_label')

plt.show()
