'''
Created on Jul 16, 2021

@author: admin
'''
tpl = (3, 4, 5, 2, 5, 1, 5)
ele = int(input('Enter element to search - '))

if ele in tpl :
    #ind = tpl.index(ele)
    for i in range(len(tpl)) :
        if tpl[i] == ele :
            print('{0} is at index {1}'.format(ele, i))
            break
else :
    print('{0} is not a member of {1}'.format(ele, tpl))
