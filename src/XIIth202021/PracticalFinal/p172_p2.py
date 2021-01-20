#MassConversion.py
'''
Created on Jan 19, 2021
Create a module MassConversion.py that stores function
for mass conversion.
@author: admin
'''
#function
def kgtotones(weight):
    "Returns : weight converted into Tones "
    return weight*kg_tone

#function
def tonestoKG(weight):
    "Returns : weight converted into KG "
    return weight/kg_tone

#function
def kgtopound(weight):
    "Returns : weight converted into Pound "
    return weight*kg_pound

#function
def poundtokg(weight):
    "Returns : weight converted into KG "
    return weight/kg_pound

#Constants
kg_tone = 0.001
kg_pound = 2.20462