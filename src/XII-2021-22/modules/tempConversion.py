# tempConversion.py
'''
Created on Aug 26, 2021
Conversion function between fahrenheite and centigrade
@author: admin
@class : 12 Computer science
@School : JNV Bokaro
'''

# functions


def to_centigrade(x):
    '''Returns : x converted to centigrade'''
    return 5 * (x - 32) / 9.0


def to_fahrenheite(x):
    '''Returns : x converted to fahrenheite'''
    return 9 * x / 5.0 + 32


# constants
freezing_c = 0.0  # water freezing temprature(in centigrade)
freezing_f = 32.00  # water freezing temprature(in fahrenheite)
