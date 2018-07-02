# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import random

percent = 100
sizes = []
colors = ["red","orange","yellow","green","blue",
          "Indigo","purple","white","gray","black"]
labels = ["A Cup","B Cup","C Cup","D Cup","E Cup",
          "F Cup","G Cup","H Cup","I Cup","J Cup"]

while percent > 10:
    rand = random.randint(10,percent)
    if percent < 10:
        break
    elif  rand < 10 :
        continue
    else:
        percent -= rand    
        sizes.append(rand)

if percent!=0:
    sizes.append(percent)
plt.pie(sizes,colors=colors,startangle = 0 ,labels = labels[:len(sizes)])
plt.title('Pie Chart')
plt.legend(title='Legend',loc = "lower left")
plt.axis('equal')

plt.show

    
    
    
    


