# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible with no remainder by all of the numbers from 1 to 20?

#Sprawdź wszystkie dzielniki najwyższej liczby. Największy dzielnik przepisz na listę pomocniczą i go odrzuć
# Jeżeli dzielnik jest w dalszej części listy, odrzuć jego pozostałe wystąpienia.


def divisors(number):
    table = [val for val in range(11) if val % 2 == 0]
    # table = []
    # for i in range(number,1,-1):
    #     if number % i == 0:
    #         table.append(i)
    # return table




print(divisors(10))

# num = 10
# num_list = [x for x in range(num,0,-1)]
# div_list = []
# print(num_list)








