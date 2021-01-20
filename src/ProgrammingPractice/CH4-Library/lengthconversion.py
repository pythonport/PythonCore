'''
Created on Jul 23, 2019

@author: admin
Module - lengthconversion.py
'''


# function
def miletokm(mile):
    '''
    Returns : km value converted from mile
    '''
    km = mile * 1.609344
    return km


# function
def kmtomile(km):
    '''
    Returns : mile value converted from km
    '''
    mile = km / 1.609344
    return mile

# function
def feettoinches(feet):
    '''
    Returns : feet value converted from inches
    '''
    inches = feet * 12
    return inches


# function
def inchestofeet(inch):
    '''
    Returns : inches value converted from feet
    '''
    feet = inch / 12
    return feet
