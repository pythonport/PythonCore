fout = open('jangalbook.txt', 'r')
'''
#no of Lines using readlines() function
lines = fout.readlines()
nooflines = len(lines)
print('number of lines are - ',nooflines)

#no of Lines with counter variable
linecount = 0
for line in fout:
    linecount+=1
print('number of lines are - ',linecount)
'''

str = ' '
linecount = 0
while str :
    str = fout.readline()
    linecount+=1
print('number of lines are - ',linecount)
print('outside')
