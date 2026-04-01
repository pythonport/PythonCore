'''
Created on Mar 19, 2026

@author: admin
'''
emp = {"Arv": (85000,90000),"Ria": (78000,88000),"Jay": (72000,80000),"Tia":(80000,70000)}
selected = []
for name in emp:
    salary = emp[name]
    average = (salary[0]+salary[1])/2
    if average>80000 :
        selected.append(name)
print(selected)