'''
Created on Aug 27, 2019

@author: admin
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 5, 6)
y = np.log(x)

plt.xlabel('6 points between [1-5]')
plt.ylabel('Log value of x variable')
plt.plot(x,y)
plt.show()