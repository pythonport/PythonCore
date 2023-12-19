'''
Created on Dec 5, 2023

@author: Admin
'''
meal = {'sun': {'breakfast':'poha', 'lunch':'roti sabji', 'dinner':'roti sabji'},
'mon': {'breakfast':'rice fri', 'lunch':'curd rice', 'dinner':'roti sabji'},
'wed': {'breakfast':'puri sabji', 'lunch':'lemon rice', 'dinner':'roti sabji'},
'thu': {'breakfast':'bread milk', 'lunch':'dal chawal chokha', 'dinner':'roti sabji'},
'fri': {'breakfast':'kachouri', 'lunch':'rice dalfri', 'dinner':'roti sabji'},
'sat': {'breakfast':'rice fri', 'lunch':'khichri', 'dinner':'roti sabji'}}

print('***Day name [sun,mon,wed,thu,fri,sat]***')
day = input('Enter date to get menu - ')
if day == 'sun':
    print('Meal Menu')
    print('-'*20)
    print('breakfast =>',meal['sun']['breakfast'])
    print('lunch =>',meal['sun']['lunch'])
    print('dinner =>',meal['sun']['dinner'])
    print('-'*20)
    
elif day == 'wed':
    print(meal['wed'])
elif day == 'thu':
    print(meal['thu'])
else:
    print('TODAY NO MEAL')
