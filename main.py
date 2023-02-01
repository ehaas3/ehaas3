"""
CMPS 6100  Lab 1
Author: Emily Haas
"""

### the only imports needed are here
import math
import time
###



def is_divisible_by(num, i):
    if (num % i == 0):
        print("True")
    else:
        print("False")



def is_prime(num):
    prime = "True"
    for i in range(2,int(math.sqrt(num)+1)):
            if (num%i == 0):
                prime = "False"
    
    return prime  



def generate_primes(upperBound):
    primes = []
    for i in range(2,upperBound+1):
        if is_prime(i) == "True":
            primes.append(i)
    return primes 
            
     

def count_primes(upper_bound):
    return len(generate_primes(upperBound))



def generate_twin_primes(upperBound):
    primes = generate_primes(upperBound)
    pairs = []
    for i in range(len(primes)):
        if i > 0:
            prev = i-1
            current = primes[i]
            previous = primes[prev]
            if current-previous == 2:
                pairs.append([previous, current])
    return pairs



def count_twin_primes(upper_bound):
    return len(generate_twin_primes(upperBound))




#########    #########
### Test Functions ###
#########    #########

# You can run them on the terminal.
# The command:
#
# pytest main.py::test_is_divisible_by
#
# Will run the test_is_divisible_by test function.

def test_is_divisible_by():
    assert is_divisible_by(2, 2) == True
    assert is_divisible_by(3, 2) == False
    assert is_divisible_by(47, 7) == False

def test_is_prime():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 241, 461, 701, 881, 883, 997]
    for prime in primes:
        assert is_prime(prime) == True
    composites = [4, 6, 8, 9, 10, 25, 30, 36, 39, 49, 60, 64, 121]
    for composite in composites:
        assert is_prime(composite) == False

def test_count_primes():
    assert count_primes(10) == 4
    assert count_primes(100) == 25
    assert count_primes(1000) == 168
    assert count_primes(10000) == 1229

def test_count_twin_primes():
    assert count_twin_primes(10) == 2
    # The two pairs less than 10 are (3,5) and (5,7)
    assert count_twin_primes(100) == 8
    assert count_twin_primes(1000) == 35
    assert count_twin_primes(10000) == 205