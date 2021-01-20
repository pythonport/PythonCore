'''
Created on Sep 13, 2019

@author: admin
'''
import numpy as np
import matplotlib.pyplot as plt

val = [[5.,25.,45,20.],[5.,23.,49,17.],[6.,22.,47,19.]]
x = np.arange(4)

plt.bar(x+0.0, val[0], color='b', width=0.25, label='range1')
plt.bar(x+0.25, val[1], color='g', width=0.25, label='range2')
plt.bar(x+0.50, val[2], color='r', width=0.25, label='range3')

plt.legend(loc="center")
plt.title("MultRange with Legend")
plt.xlabel("X Label")
plt.ylabel("Y Label")
#plt.savefig("C:\\Users\\admin\\Desktop\\Bokaro\\MultiBar.pdf")
plt.show()