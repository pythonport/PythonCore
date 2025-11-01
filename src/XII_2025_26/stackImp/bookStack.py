'''
Created on Sep 10, 2025
Stack implementation using book object
@author: admin
'''
BooksStack =[]

def push_book(BooksStack, new_book):
    BooksStack.append(new_book)

def pop_book(BooksStack):
    if len(BooksStack)== 0 :
        return "Underflow"
    else :
        return BooksStack.pop()
    
def peep(BookStack) :
    if len(BooksStack)== 0 :
        return 'None'
    else :
        return BookStack[-1]

book = ['computer science','sumita arora','2025']
push_book(BooksStack, book)

pop_book(BooksStack)

print(peep(BooksStack))