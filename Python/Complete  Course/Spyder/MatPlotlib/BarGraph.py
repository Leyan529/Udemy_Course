# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt  #視覺化資料模組
import numpy as np #數學庫
import random

list = []
for i in range(0,10,1):
    ran = random.randrange(0,30)
    list.append(ran)

t = tuple(list)
pos = np.arange(10) + 0.5
plt.barh(pos,tuple(list) , align ='center',color = 'red')

plt.xlabel('Height in Inches', color = "Red")
plt.ylabel('Students',  color ='Red')
plt.title('Height in Students', color = 'blue' )

plt.tick_params(axis = 'x', colors = 'black')
plt.tick_params(axis = 'y', colors = 'black')


name = ['April','BTOB','CLC','EXID','GFreind'
        ,'Infinte','AOA','BTS','BlackPink','Twice']
plt.yticks(pos,name)

plt.subplots_adjust(left = .20 ,bottom = .20, right=.94)

plt.show