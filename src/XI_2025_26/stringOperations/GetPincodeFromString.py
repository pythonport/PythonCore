'''
Created on Feb 5, 2026
Get pincode from string
@author: admin
'''
address = input('Place name with pin code - ')
i=0
ln = len(address)
while i < ln:
    ch = address[i]
    if ch.isdigit():
        sub = address[i :i+6]
        if sub.isdigit() and len(sub)==6:
            print('pincode -',sub)
            break
    i+=1
else :
    print("No pin code found")