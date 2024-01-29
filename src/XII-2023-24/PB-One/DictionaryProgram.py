'''
Created on Jan 4, 2024

@author: Admin
'''
books = {1:"Python", 2:"Internet Fundamentals ", 3:"Networking ",
4:"Oracle sets", 5:"Understanding HTML"}

def dispBook(BOOKS):
    vowels = ['A','E','I','O','U']
    for i in books :
        if books[i][0] not in vowels :
            print(books[i].upper())