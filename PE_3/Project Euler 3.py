# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

from math import sqrt

number = int(input('What number to factor?   '))
list_of_factors = [1]
for _ in range(2, int(sqrt(number))):
    if number % _ == 0:
        list_of_factors.append(_)
        _ = 2
        number = number / _

print(list_of_factors)

