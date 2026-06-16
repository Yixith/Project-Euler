# n! means n * (n - 1) * ... * 3 * 2 * 1.
# For example, 10! = 10 * 9 *  * 3 * 2 * 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!.


def factorial(number):
    num = 1
    for i in range(1, number + 1):
        num *= i
    return num

digits = str(factorial(100))
lista = [int(x) for x in digits]

print(sum(lista))