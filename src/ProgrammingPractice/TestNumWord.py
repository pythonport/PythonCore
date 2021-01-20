'''
Created on Aug 6, 2019

@author: admin
'''


num = 1001
nums_dict = {100: 'hundred', 1000:'thousand', 1000000:'million', 1000000000:'billion'}

print([key for key in nums_dict.keys() if key <= num])
maxkey = max([key for key in nums_dict.keys() if key <= num])
print(maxkey)