'''
Created on Aug 27, 2019

@author: admin
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
a = np.cos(x)
b = np.sin(x)
plt.plot(x, a, '#FF8778', linewidth=4, linestyle='solid')  # dotted   dashed  dashdot
plt.plot(x, b, 'c')
plt.show()
