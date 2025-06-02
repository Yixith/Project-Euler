#If we list all the natural numbers below 10 that are multiples 
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

max_number = int(input('What is highest number needed for this task?'))

list_of_numbers = (num for num in range(max_number) if num % 3 == 0 or num % 5 == 0)
sum_of_multiples = 0
for i in list_of_numbers:
    sum_of_multiples = sum_of_multiples + i
print(sum_of_multiples)
