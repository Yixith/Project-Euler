#  The following iterative sequence is defined for the set of positive integers: 
#  n ->  n / 2 (n is even)
#  n ->  3n + 1 (n is odd) 
#  Using the rule above and starting with  13 , we generate the following sequence:
#  13 -> to 40 -> to 20 -> to 10 -> to 5 -> to 16 -> to 8 -> to 4 -> to 2 -> to 1.   
#  It can be seen that this sequence (starting at  13  and finishing at  1 ) contains  10  terms.
#  Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers 
#  finish at  1. 
#  Which starting number, under one million, produces the longest chain? 
#  NOTE: Once the chain starts the terms are allowed to go above one million. 

base = {1:4, 2:1, 4:2, 13:40}

def collatz(number):
    while number > 1:
        if number in base:
            break
        elif number % 2 == 0:
            base.update({number: int(number/2)})
            number = int(number / 2)        
        else:
            base.update({number: int(3 * number + 1)})
            number = int(3 * number + 1)

        # return number
            
for i in range(999999,1, -1):
    collatz(i)
print(base)




# for i in range(999999, 1, -1):


    
