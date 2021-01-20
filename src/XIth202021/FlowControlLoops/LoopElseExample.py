'''
Created on Jan 18, 2021
LoopElse Example
@author: admin
'''
for i in range(1,11) :
    if i==5:
        break
        #continue
    else :
        print(i)
else:
    print('I am happy in for')
    
    
print("Else with while loop")
a = 1
while a<11:
    a+=1
    if a==5:
        #break
        continue
        #pass
    else :
        print(a)
else:
    print('I am happy in while')
    
    
print('===============')
while 3>4 :
    print("coming to while loop")
else :
    print("Loop else of while")