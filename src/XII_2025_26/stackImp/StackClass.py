'''
Created on Sep 9, 2025

@author: admin
'''
class stack :
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        self.stack.pop()
    
    def peek(self):
        if self.isEmpty() :
            return 'stack is empty'
        return self.stack[-1]
    
    def isEmplty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)

mystack = stack()
mystack.push('A')
mystack.push('B')
mystack.push('C')

print('Stack : ',mystack.stack)
print('Pop : ',mystack.stack.pop())
print('Stack after pop: ',mystack.stack)
print('Peak: ',mystack.peek())
print('isEmpty: ',mystack.isEmplty())
print('size: ',mystack.size())