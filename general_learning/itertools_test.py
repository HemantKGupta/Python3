import itertools

letters = ['a', 'b', 'c', 'd', 'e', 'f']
booleans = [1, 0, 1, 0, 0, 1]
numbers = [23, 20, 44, 32, 7, 12]
decimals = [0.1, 0.7, 0.4, 0.4, 0.5]

# usage of chain
print(list(itertools.chain(letters,booleans)))

# usage of count
for i in itertools.count(10, 0.25):
    if i < 20:
        print(i)
    else:
        break

# permutations
#print(list(itertools.combinations('12345',2)))

a = [1,2,3,4]
p = itertools.permutations(a)
#print(p.next())
#print(p.next())
#print(list(itertools.permutations('ABCD', 2)))
permutations = []
for item in itertools.permutations('dhck'):
    permutations.append(''.join(item))
print(permutations)
sorted_permutations = sorted(permutations)
print(sorted_permutations)
index_original = sorted_permutations.index('dkhc')
print(sorted_permutations[index_original+1])

#print(''.join(list((itertools.permutations('hefg'))[0])))
#print(list(itertools.permutations('hefg'))[1])
#print(list(itertools.permutations('hefg'))[2])
#new_list = [' '.join(words) for words in list(itertools.permutations('hefg'))[1]]
#print(''.join(new_list))

