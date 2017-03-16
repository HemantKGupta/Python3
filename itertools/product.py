from itertools import product
#print(list(product([1,2,3],repeat = 2)))

A = [1, 2]
B = [3, 4]
#print(list(product(A, B)))

from itertools import product
a = input()
a_str = a.split(' ')
a_list = list(map(int, a_str))
b = input()
b_str = b.split(' ')
b_list = list(map(int, b_str))
out = list(product(a_list, b_list))
for item in out:
    print(item, end=' ')