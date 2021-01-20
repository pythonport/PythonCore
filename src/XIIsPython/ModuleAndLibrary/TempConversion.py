'''
Created on Jul 8, 2019
Code with conversion functions between fahrenheit and Centrigrade
@author: admin
Module - TempConversion.py
'''

#functions
def to_centigrade(x):
    '''
    Returns : x conerted to centigrade
    '''
    return 5*(x-32)/9.0

def to_fahrenheit(x):
    '''
    Returns : x conerted to fahrenheit
    '''
    return 9*x/5.0+32

def __HelloTempConversion():
    '''
    Return : void private method declared
    '''
    print("Hello TempConversion Program")

#constants
FREEZING_C = 0.0  #water freezing temprature.(in Centrigrade)
FREEZING_F=32.0  #water freezing temprature.(in fahrenheit)