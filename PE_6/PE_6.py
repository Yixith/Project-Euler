# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_squares(num):
    nums = [y ** 2 for y in range(1,num + 1)]
    x = sum(nums)
    return x

def square_of_sum(num):
    nums = [y for y in range(1, num + 1)]
    x = sum(nums)
    x = x ** 2
    return x


def square_minus_sum(num):
    return square_of_sum(num) - sum_of_squares(num)


number = 100
print(square_minus_sum(number))