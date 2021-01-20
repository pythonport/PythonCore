'''
Created on Jan 16, 2021
Write a function that receives two numbers and generates a random
number from that range. Using this function, the main program should
be able to print three number randomly.
@author: admin
'''
import random


def generateRandom(a, b):
    return random.randint(a, b)


a, b = 8, 18
print("Random 1 - ", generateRandom(a, b))
print("Random 2 - ", generateRandom(a, b))
print("Random 3 - ", generateRandom(a, b))