# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import random
fig = plt.figure()

#set back-ground color
rect = fig.patch
rect.set_facecolor('green') 

x = []
y = []
for i in range(0,4):
  x.append(random.randrange(0,30))  
  y.append(random.randrange(0,30)) 

#編碼為單個整數的subplot網格參數
#  axisbg為網格背景顏色
graph1 = fig.add_subplot(1,1,1,axisbg='black') #fig.add_subplot(wedith,height) 
graph1.plot(x,y,'red',linewidth = 4.0) #畫線資訊

graph1.tick_params(axis='x',color ="white") #顯示x軸刻度
graph1.tick_params(axis='y',color ="white") #顯示y軸刻度

graph1.spines["top"].set_color('w')     #視窗邊線
graph1.spines["left"].set_color('w')
graph1.spines["right"].set_color('w')
graph1.spines["bottom"].set_color('w')

graph1.set_title("Random Graph" , color = 'white') #標題
graph1.set_xlabel('X - axis', color = 'white')  #X軸標題
graph1.set_ylabel("Y - axis", color = 'white')  #Y軸標題




plt.show


