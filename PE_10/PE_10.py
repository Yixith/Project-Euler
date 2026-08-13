# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def sieve(n):
    if n < 2:
        return []
    
    primes = [True for x in range(n+1)]

    primes[0] = primes[1] = False

    for i in range(2,int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return [i for i in range(n + 1) if primes[i]]

print(sum(sieve(2000000)))