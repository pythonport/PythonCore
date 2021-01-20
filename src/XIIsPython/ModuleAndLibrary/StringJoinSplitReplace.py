'''
Created on Jul 11, 2019

@author: admin
'''
nm = 'JAWAHAR'
print('***'.join(nm))

word = "120*Mukesh Kumar*34.5"

lword = word.split('*')
print('Rollno %s whose name is %s secured %s marks' % (lword[0], lword[1], lword[2]))

print(word.replace('*','#'))
