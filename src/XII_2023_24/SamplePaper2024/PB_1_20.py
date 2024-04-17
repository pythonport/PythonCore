'''
Created on Dec 29, 2023

@author: Admin
'''
company=['Bajaj','Benz','Maruti','Hero','Hyundai']
def replacecompany(company) :
    for i in range(len(company)):
        if company[i][1]=='a' :
            company[i] = 'xyz'

print(company)
replacecompany(company)
print(company)