# Patrick Roscio
# February 6th, 2024
# Lab_3 oddSums.py

import random

l_bound = random.randrange(1,10)
h_bound = random.randrange(11,20)

print(f"The lower bound is {l_bound} and the higher bound is {h_bound}.")

index = l_bound
sum = 0

while index <= h_bound:
    if index % 2 == 1:
        sum += index
        print (index)
        index +=1
    else:
        index +=1
else:
    print (f"The sum is {sum}.")
