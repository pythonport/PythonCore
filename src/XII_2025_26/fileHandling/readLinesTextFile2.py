# Second way to read file with file object only whout using read function
fout = open('jangalbook.txt', 'r')
for line in fout :
    print(line)
