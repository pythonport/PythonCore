'''
Created on Dec 26, 2024

@author: admin
'''
marks = int(input('Enter marks - '))
if marks>= 80 :
    print('you scored - ',marks)
    print("Passed with more then 80")
elif marks >=60 :
    print('you scored - ',marks)
    print("Passed with more then 60 but less then 80")
elif marks >=45 :
    print('you scored - ',marks)
    print("Passed with more then 45 but less then 60")
elif marks >=33 :
    print('you scored - ',marks)
    print("Passed with more then 33 and just passed")
else :
    print('Sorry')