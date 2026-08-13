# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?



rot_primes = []
def sieve(n):
    if n < 2:
        return []

    is_prime = [True for _ in range(n + 1)]
    is_prime[0] = is_prime[1] = False 

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False 

    return [i for i, val in enumerate(is_prime) if val]


sito = sieve(1000000)

sito_set = set(sito)

def number_rotation(n):
    rot_nums = []
    var = str(n)
    for i in range(len(str(n))):
        var = var[-1:] + var[:-1]
        if int(var) in sito_set:
            rot_nums.append(int(var))
        else:
            rot_nums = []
            break
    return rot_nums

def number_write(n):
    if len(str(n)) == 1:
        rot_primes.append(n)
    else:
        var = number_rotation(n)
        rot_primes.extend(var)


for i in sito:
    number_write(i)
    
rot_primes = set(rot_primes)
rot_primes = list(rot_primes)
rot_primes.sort()
print(rot_primes, len(rot_primes))