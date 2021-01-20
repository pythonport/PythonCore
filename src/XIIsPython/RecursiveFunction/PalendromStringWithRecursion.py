'''
Created on Jan 8, 2020

@author: admin
'''
word = input("Enter word to check palindrom string - ")


def palindromCheck(word):
    length = len(word)
    
    if length == 0 or length == 1:
            return "Palindrom String"
    elif word[0] == word[length - 1] :        
        return palindromCheck(word[1:length - 1])        
    else :
        return "Not Palindrom String"


status = palindromCheck(word)    
print("{0} is {1}".format(word, status))
