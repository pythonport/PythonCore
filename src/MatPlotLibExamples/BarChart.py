'''
Created on Apr 18, 2019

@author: admin
'''

import matplotlib.pyplot as pyplot
from django.core.management import color
from Tools.demo.sortvisu import WIDTH
lstdays = ['MON','TUE','WED','THU','FRI','SAT']
lstatt = [34,15,33,96,57,32]
#pyplot.plot(lstdays,lstatt,'red')

#pyplot.bar(lstdays, lstatt,WIDTH=0.5,color=["orange",'red','green'])

'''
pyplot.xlabel("Days of Week")
pyplot.ylabel("Students attendence")
pyplot.title("Attendence of Student of this week")
'''
pyplot.pie(lstatt,labels=lstdays, colors=["orange",'red','green','blue'],autopct='%1.1f%%')
pyplot.show()