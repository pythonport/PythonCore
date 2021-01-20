'''
Created on Jul 24, 2019

@author: admin
'''


def copyOnlyAtheletics(sports, asports):
    fin = open(sports, 'r')
    fout = open(asports, 'w')
    str = ' '
    while str :
        str = fin.readline()
        lstr = str.split('~')
        if lstr[0] == 'Atheletics':
            fout.write(str)

    fin.close()
    fout.close()


sfile = 'sports.txt'
afile = 'Atheletics.txt'
copyOnlyAtheletics(sfile, afile)

with open(afile, 'r') as fin :
    print(fin.read())
