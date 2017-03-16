from collections import Counter
lis = [1, 2, 2, 3, 4, 4, 4]
print(Counter(lis))
print(Counter(lis).items())
print(Counter(lis).values())
print(Counter(lis).keys())
c = Counter(lis)
print(c[4])