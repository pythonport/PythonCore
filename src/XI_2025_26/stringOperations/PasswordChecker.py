'''
Created on Feb 5, 2026
rule for user name - starts with jnvd like jnvd123
rule for password - it must be alphanumaric value
@author: admin
'''
uname = input('User name - ')
pword = input('Password - ')
if not uname.startswith('jnvd'):
    print('Invalid user name, must starts with jnvd')

if not pword.isalnum() :
    print('Invalid password it must be alphanumaric value')

if uname=='jnvd123' and pword=='password123' :
    print('Login success')
else :
    print('Invalid username and password! Try again')