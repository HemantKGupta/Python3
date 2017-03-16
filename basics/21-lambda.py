seq = [1,2,3,4, 5]
def times2(item):
    return 2*item
print(list(map(times2, seq)))


x = lambda var: var*2
print(x(6))

print(list(map(lambda item: item*2, seq)))

print(list(filter(lambda item: item%2 == 0, seq)))

