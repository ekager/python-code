import timeit
from math import sqrt
import sys


#sum of factors excluding itself equals n
def perfect(n):
    sum = 0
    x = 1
    while (x < n):
        if (n%x == 0):
            sum = sum + x
        x = x + 1
    return (sum == n)

     
#Prime number checker -> no factors excluding 1 and itself
def prime(n):
    i = 2
    while (i<(n-1)):
        if (n%i == 0):
            return False
        i = i + 1
    if (n < 2):
        print("Please give number greater than 2")
        return
    if (n <= 3):
        return True
    return True

c = list(range(2, 100))

def perfcheck(c):
    start = timeit.default_timer()
    for x in c:
        if (perfect(x) == True):
            print(x)
    stop = timeit.default_timer()
    print(stop - start)

#my generator method
def primegen(c):
    start = timeit.default_timer()
    for x in c:
        if (prime(x) == True):
            print(x)
    stop = timeit.default_timer()
    print(stop - start)

#Python prime generator using sieve approach found with research
def primes_sieve1(limit):
    start = timeit.default_timer()
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    stop = timeit.default_timer()
    print(stop - start)
    return [i for i in primes if primes[i]==True]


#much shorter perfect number found with research
def ifactors(n):
    return [i for i in range(2, (n//2)+1) if n % i == 0]

def perfect2(n):
    return [i for i in range(2, n+1) if sum(ifactors(i)) + 1 == i]