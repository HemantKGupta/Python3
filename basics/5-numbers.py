import random

print("choice([1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9]))
print("choice('A String') : ", random.choice('A String'))

aList = [20, 16, 10, 5];
random.shuffle(aList)
print("Reshuffled list : ",  aList)
