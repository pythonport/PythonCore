'''
Created on Aug 25, 2025

@author: admin
'''
import pickle
s1 = {'rollno':1,'name':'Sia','marks':87.5}
s2 = {'rollno':2,'name':'Raghu','marks':77.5}
s3 = {'rollno':3,'name':'Harish','marks':75.5}
s4 = {'rollno':4,'name':'Ketan','marks':92.5}

fh = open('stufee.dat','wb')
pickle.dump(s1, fh)
pickle.dump(s2, fh)
pickle.dump(s3, fh)
pickle.dump(s4, fh)
fh.close()
print('done')