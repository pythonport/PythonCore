'''
Created on Dec 29, 2020
Write a function AMCount() in Python, 
which should read each character of a text 
file STORY.TXT, should count and display the 
occurance of alphabets A and M 
(including small cases a and m too).
@author: admin
'''


def countAndM():
    fout = open('story.txt', 'r')
    aCount = 0
    mCount = 0
    data = fout.read()
    aCount = data.find('A') + data.find('a')
    mCount = data.find('M') + data.find('m')
    
    print("Total count of A or a - ", aCount)
    print("Total count of M or m - ", mCount)
    
    fout.close()

    
def countAndMWithLoop():
    fout = open('story.txt', 'r')
    aCount = 0
    mCount = 0
    data = fout.read()
    for i in data :
        print(i)
        if i == 'A' or i == 'a':
            aCount += 1
        elif i == 'M' or i == 'm':
            mCount += 1
    
    print("Total count of A or a - ", aCount)
    print("Total count of M or m - ", mCount)
    
    fout.close()


countAndMWithLoop()
