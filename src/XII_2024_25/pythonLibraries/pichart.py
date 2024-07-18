'''
Created on Jul 16, 2024
This file has been created to demonstrate the use of pie function 
of matplotlib
@author: admin
'''
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15,35, 25, 25, 15])
plt.pie(y)
plt.show()