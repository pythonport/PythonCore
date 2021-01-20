'''
Created on Feb 28, 2019
GCD and LCM are not in math module.
Calculation of GCD and LCM with own logic.
@author: admin
'''
def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)
                       
if __name__ == "__main__":
    # execute only if run as a script
    n = int(input("Enter first number - "))
    m = int(input("Enter second number - "))
    
    gcdval = gcd(n, m)    
    lcmval = lcm(n, m)
    
    print ('GCD of ', n ,' and ',m, ' is = ',gcdval)
    print ('LCM of ', n ,' and ',m, ' is = ',lcmval)