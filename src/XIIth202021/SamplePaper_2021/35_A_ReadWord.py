'''
Created on Dec 29, 2020
Write a function in Python that counts the number 
of Me or My words present in a text file STORY.TXT.
@author: admin
'''
def countMeMy():
    fout = open('story.txt', 'r')
    count = 0
    data = fout.read()
    ldata = data.split()
    for a in ldata :
        if a == 'Me' or a == 'My' :
            count += 1
    print("Total count of my and me is - ", count)
    fout.close()

countMeMy()