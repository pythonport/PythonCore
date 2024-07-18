'''
Created on Apr 17, 2024

@author: admin
'''


def interest(prin, rate=10, time=5):
    si = (prin * rate * time) / 100
    print("simple interest  - ", si)


interest(5000, 8, 5)  # required or positional call
interest(time=10, prin=4000, rate=6)  # keyword call
interest(rate=6, time=10, prin=4000)  # keyword call

interest(5000, time=7)  # combination of all type of argument
