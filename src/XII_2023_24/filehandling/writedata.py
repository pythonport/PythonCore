'''
Created on Jul 26, 2023

@author: acer
'''
fout = open('exam.txt','w')
dayfirst = '1.chemistry, phe'
daysecond ='2.physics, english'
daythird = '3.math, computer'
fout.write(dayfirst)
fout.write(daysecond)
fout.write(daythird)
fout.close()
print('writing is done')