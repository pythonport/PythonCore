'''
Created on Jul 29, 2021

@author: admin
'''


def simpleInterest(principal=500, time=6, rate=10):
    print("Principal Amount - ", principal)
    print("Time is - ", time)
    print("Rate is - ", rate)
    si = (principal * time * rate) / 100
    return si


interest = simpleInterest(rate=9, principal=400, time=2)
print("Simple interest is - ", interest)

p, t, r = 400, 5, 8
interest = simpleInterest(p, t, r)
print("Simple interest is - ", interest)

interest = simpleInterest(4000, 5, 6)
print("Simple interest is - ", interest)

interest = simpleInterest(2000, 5)
print("Simple interest is - ", interest)

interest = simpleInterest(1000)
print("Simple interest is - ", interest)

interest = simpleInterest()
print("Simple interest is - ", interest)
