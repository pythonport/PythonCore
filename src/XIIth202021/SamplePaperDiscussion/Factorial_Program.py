n = int(input("Enter any number - "))

fact = 1
for a in range(1, n+1):
    fact *= a
    print("factorial of {} is  - {}".format(a, fact))

print("factorial of {} is  - {}".format(n, fact))