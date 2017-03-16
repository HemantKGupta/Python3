tup = ('physics', 'chemistry', 1997, 2000);

print(tup)
del tup;
print("After deleting tup : ")
#print(tup)

tuple = ('hi',)   ## size-1 tuple

tuple = (1, 2, 'hi')
tuple = (1, 2, 'bye')  ## this works

(x, y, z) = (42, 13, "hike")
print(z)

#List Comprehensions
nums = [1, 2, 3, 4]
squares = [ n * n for n in nums ]   ## [1, 4, 9, 16]

strs = ['hello', 'and', 'goodbye']
shouting = [ s.upper() + '!!!' for s in strs ]