import math
import time

check = False
test = 0

prime_list = [2]

#func prime_check: Function that uses mod to check prime
def prime_check(num):
    if num < 2:
        return False
    if num in prime_list:
        return True
    for i in prime_list:
        if num % i == 0:
            return False
    prime_list.append(test)
    return True

def prime_all(a):
    if a == True: print(str(test) + " is prime")
    else:
        print(str(test) + " is not prime")

x = 100000
print()
print("Checking: " + str(x))
while test < x:
    prime_check(test)
    test += 1
if prime_check(x):
    print(str(x) + " is prime")
else:
    print(str(x) + " is not prime")
