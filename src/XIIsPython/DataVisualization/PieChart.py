'''
Created on Sep 12, 2019

@author: admin
'''
import matplotlib.pyplot as plt

data =  [13,60,17,15]
lblmovie=['Breakfast','Movie','CycleStand','ColdDrink']
lblcolor=['#FF9933','yellow','green','#00FFAA']
lblexplod = [0.1,0,0,0.15]
plt.pie(data,labels=lblmovie, autopct='%1.2f%%', colors=lblcolor, explode=lblexplod)
plt.show()