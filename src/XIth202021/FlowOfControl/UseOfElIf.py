'''
Created on Jan 7, 2021

@author: admin
'''
marks = int(input("Enter marks of student - "))
if marks >= 75 :
    print('First division with gold madel')
elif marks >= 60 :
    print('First division')
elif marks >= 33:
    print("Passed")
else:
    print("Failed")
    
print("I am done")