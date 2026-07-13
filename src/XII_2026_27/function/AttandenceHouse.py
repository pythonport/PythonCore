'''
Created on Apr 20, 2026

@author: admin
'''
att = {"Arawali":0,"Nilgiri":0,'Shivalik':0,'Udayagiri':0}

def getAttandence():
    for key in att :
        count = input(f'Enter attandance for {key} - ')
        att[key] = count
    
def printAttandance():
    for key in att :
        print(f'{key}->{att[key]}')
    

print(att)
getAttandence()
printAttandance()