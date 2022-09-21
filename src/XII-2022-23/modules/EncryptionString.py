'''
Created on Aug 24, 2022

@author: admin
'''
def encrypt(str, enkey) :
    return enkey.join(str)

def decrypt(str, enkey) :
    return str.split(enkey)

mainStr = input('Enter String to be encrypted- ')
encrCode = input('Enter Code to encrypt- ')
encrpytStr = encrypt(mainStr, encrCode)
print("Encrypted String is - ",encrpytStr)
lstDecrupt = decrypt(encrpytStr,encrCode)
print("Decrypted List is - ",lstDecrupt)
deStr = ''.join(lstDecrupt)
print("Decrypted String is - ",deStr)
