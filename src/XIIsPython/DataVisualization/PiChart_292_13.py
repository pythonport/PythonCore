'''
Created on Nov 26, 2019

@author: admin
'''

import matplotlib.pyplot as plt

con = [23.4,17.8,25,38,40]
zone= ['EAST','WEST','NORTH','SOUTH','CENTRAL']
plt.axis('equal')
plt.pie(con,labels=zone, explode=(0,0,0.2,0,0),autopct='%1.2f%%')
plt.show()