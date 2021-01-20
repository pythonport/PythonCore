'''
Created on Dec 31, 2020
Write a program that generates six random
numbers in a sequence created with (start, stop, step).
Then print the mean, median and mode of the generated numbers.
@author: admin
'''
import random
import statistics

r1 = random.randrange(10, 50, 4)
r2 = random.randrange(10, 50, 4)
r3 = random.randrange(10, 50, 4)
r4 = random.randrange(10, 50, 4)
r5 = random.randrange(10, 50, 4)
r6 = random.randrange(10, 50, 4)
print(r1, r2, r3, r4, r5, r6)
lstOfRandom = [r1, r2, r3, r4, r5, r6]

mean = statistics.mean(lstOfRandom)
median = statistics.median(lstOfRandom)
mode = statistics.mode(lstOfRandom)
print("Mean Value is  - ",mean)
print("median Value is  - ",median)
print("mode Value is  - ",mode)