'''
Created on Sep 9, 2024

@author: admin
'''
with open('namesoflanguages.txt','w') as fout :
    fout.write('Python\n')
    fout.write('Java\n')
    fout.write('C++\n')
    fout.write('PHP\n')
    fout.write('Pearl')
    
fout.write('data science') #this line with throw error
print('Writing done')