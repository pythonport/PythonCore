'''
Created on Aug 30, 2019

@author: admin
'''
import matplotlib.pyplot as plt
import numpy as np
a = np.arange(1, 5)
b = a * 2
c = a ** 2
print(a)
print(b)
print(c)

plt.bar(a, c)
plt.Line2D(a,c)
#plt.bar(a+0.35, c, width=0.35)
plt.show()
