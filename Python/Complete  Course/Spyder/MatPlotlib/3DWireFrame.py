# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d #3D繪圖套件
import numpy as np
import random

fig = plt.figure()


chart = fig.add_subplot(1,1,1, projection = '3d')

x,y,z = axes3d.get_test_data(0.05)
chart.plot_wireframe(x,y,z, rstride=1,cstride=10)

chart.set_xlabel('x_label')
chart.set_ylabel('y_label')
chart.set_zlabel('z_label')

plt.show()

