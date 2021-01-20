'''
Created on Jul 24, 2019

@author: admin
'''


def convertOneLineToTwo(telone, teltwo):
    fin = open(telone, 'r')
    fout = open(teltwo, 'w')
    str = ' '
    linecount = 1
    lineToWrite = ''
    while str :
        str = fin.readline()
        print(str)
        lineToWrite += str
        linecount += 1
        if linecount == 2:
            fout.write(lineToWrite)
            str = ''
            linecount = 1

    fin.close()
    fout.close()


sfile = 'telephone.txt'
afile = 'telephone2.txt'
convertOneLineToTwo(sfile, afile)

with open(afile, 'r') as fin :
    print(fin.read())
