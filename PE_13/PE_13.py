# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.


with open ('numbers.txt','r') as f:
    nums = f.read()


result = 0
nums = nums.split('\n')
for i in nums:
    result += int(i)

print(result)