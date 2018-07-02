# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import random
import numpy as np
fig = plt.figure()

#set back-ground color
rect = fig.patch
rect.set_facecolor('green') 

x1 = []
y1 = []
x2 = []
y2 = []

for i in np.arange(-10,10,0.02):
  rx = i
  ry = np.sin(rx)
  x1.append(rx)  
  y1.append(ry)  
  ry = np.cos(rx)
  x2.append(rx)  
  y2.append(ry)


#編碼為單個整數的subplot網格參數
#  axisbg為網格背景顏色
graph1 = fig.add_subplot(2,1,1,axisbg='black') #fig.add_subplot(wedith,height) 
graph1.plot(x1,y1,'red',linewidth = 4.0) #畫線資訊

graph1.tick_params(axis='x',color ="white") #顯示x軸刻度
graph1.tick_params(axis='y',color ="white") #顯示y軸刻度

graph1.spines["top"].set_color('w')     #視窗邊線
graph1.spines["left"].set_color('w')
graph1.spines["right"].set_color('w')
graph1.spines["bottom"].set_color('w')

graph1.set_title("Random Graph" , color = 'white') #標題
graph1.set_xlabel('X - axis', color = 'white')  #X軸標題
graph1.set_ylabel("Y - axis", color = 'white')  #Y軸標題

graph2 = fig.add_subplot(2,1,2,axisbg='black') #fig.add_subplot(wedith,height) 
graph2.plot(x2,y2,'yellow',linewidth = 5.0) #畫線資訊

graph2.tick_params(axis='x',color ="white") #顯示x軸刻度
graph2.tick_params(axis='y',color ="white") #顯示y軸刻度

graph2.spines["top"].set_color('w')     #視窗邊線
graph2.spines["left"].set_color('w')
graph2.spines["right"].set_color('w')
graph2.spines["bottom"].set_color('w')

graph2.set_title("Random Graph" , color = 'white') #標題
graph2.set_xlabel('X - axis', color = 'white')  #X軸標題
graph2.set_ylabel("Y - axis", color = 'white')  #Y軸標題




plt.show

