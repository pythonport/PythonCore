'''
Created on Sep 13, 2019

@author: admin
'''
import numpy as np
import matplotlib.pyplot as plt

col = [8000,12000,9800,11200,15500,7300]
x= np.arange(6)
days=['MON','TUE','WED','THU','FRI','SAT']
sections=['A','B','C','D','E','F']
plt.title("Volunteering week collection")
#plt.xticks(x,days)
plt.xticks(x,sections)
plt.xlabel("Days")
plt.ylabel("Collection Amount")
plt.bar(x,col,color='r', width=0.25)
plt.show()