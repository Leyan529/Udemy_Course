# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import random
fig = plt.figure()

#set back-ground color
rect = fig.patch
rect.set_facecolor('green') 

x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
for i in range(0,4):
  x1.append(random.randrange(0,30))  
  y1.append(random.randrange(0,30))
  x2.append(random.randrange(10,20))  
  y2.append(random.randrange(10,20))
  x3.append(random.randrange(15,35))  
  y3.append(random.randrange(15,35)) 

#編碼為單個整數的subplot網格參數
#  axisbg為網格背景顏色
graph1 = fig.add_subplot(1,1,1,axisbg='black') #fig.add_subplot(wedith,height) 
graph1.plot(x1,y1,'red',linewidth = 4.0) #畫線資訊
graph1.plot(x2,y2,'orange',linewidth = 6.0) #畫線資訊
graph1.plot(x3,y3,'yellow',linewidth = 5.0) #畫線資訊

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
