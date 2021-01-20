'''
Created on Aug 28, 2019

@author: admin
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 6)
y = np.tan(x)
z = np.cos(x)
a = np.sin(x)

plt.title("Sin, Cos, Tan value of number")
plt.xlabel('actual number')
plt.ylabel('squred number')
#plt.xticks([0,2,4,6])
#plt.plot(x, y, marker='d', markeredgecolor='red')
plt.plot(x, y, 'ro', linestyle='solid', linewidth=6)
plt.plot(x, z, 'bo', linestyle='solid', linewidth=4)
plt.plot(x, a, 'go', linestyle='solid', linewidth=2)
plt.show()
