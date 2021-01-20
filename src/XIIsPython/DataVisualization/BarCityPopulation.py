'''
Created on Aug 30, 2019

@author: admin
'''
import matplotlib.pyplot as plt

city = ['Delhi', 'Mumbai', 'Bangalore', 'Hyderabad']
population = [23456123, 20083102, 18455123, 13411093]
#customc=['#00DD00','#AADD00','#00DDBB','#AADDFF']
customc=['#FF0000','#00FF00','#0000FF','#AADDFF']
plt.xlabel("City")
plt.ylabel("Population")
plt.bar(city, population, color=['#FF0000','#00FF00','#0000FF','#AADDFF'])
plt.show()
