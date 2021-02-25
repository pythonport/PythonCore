'''
Created on Feb 5, 2021

@author: admin
'''
line = input("Enter the line to find substring - ")
sub = input("Enter the line to find substring - ")
lenline = len(line)
lensubstr = len(sub)
start = count = 0
end = lenline

while True :
    pos = line.find(sub, start, end)
    if pos != -1 :
        count += 1
        start = pos + lensubstr
    else :
        break
    
    if start >= lenline:
        break
print("No of occurance of ", sub, " is -", count)
