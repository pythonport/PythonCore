'''
Created on Jul 16, 2021

@author: admin
'''
subjects = {'raghu':'compSc', 'Afjal':'Python', 'Deepak':'SQL', 'Riya':'English'}
sval = input('Enter subject name - ')

for a in subjects :
    if subjects[a].upper() == sval.upper() :
        print('{0} teaches {1}'.format(a, sval))
        break
else :
    print('{0} Subject is not part of dictionary'.format(sval))
