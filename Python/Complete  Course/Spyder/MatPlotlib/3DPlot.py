# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d #3D繪圖套件
import random
    
fig = plt.figure()
plot_3D = fig.add_subplot(1,1,1,projection = '3d')

x_list=[]
y_list=[]
z_list=[]

xd_list=[]
yd_list=[]
zd_list=[]

for i in range(0,9,1):    
    x_list.append(random.randint(1,10))
    y_list.append(random.randint(1,10))
    z_list.append(random.randint(1,10))
    
    xd_list.append(random.randint(-10,-1))
    yd_list.append(random.randint(-10,-1))
    zd_list.append(random.randint(-10,-1))
    
    

X,Y,Z = x_list,y_list,z_list #3維範圍
Xd,Yd,Zd = xd_list,yd_list,zd_list #3維範圍

#plot_3D.plot_wireframe(X,Y,Z)  #三維軌跡
plot_3D.scatter(X,Y,Z,c='red',marker = 'o')
plot_3D.scatter(Xd,Yd,Zd,c='blue',marker = '^')

plot_3D.set_xlabel('x_axis')
plot_3D.set_ylabel('y_axis')
plot_3D.set_zlabel('z_axis')


plt.show()