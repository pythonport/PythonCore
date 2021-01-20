'''
Created on Nov 9, 2019
Page no 156 XII (4.3)
@author: admin
'''
import random
stu1 = stu2 = stu3 = 0
#num = 1
while True :
    stu1=random.randint(1,4)
    stu2=random.randint(1,4)
    stu3=random.randint(1,4)    
    #print("Loop count = ",num)
    #num+=1
    if stu1!=stu2 and stu1!=stu3 and stu2!=stu3:
        break
    
print('Three random students are : - ',stu1,stu2,stu3)  