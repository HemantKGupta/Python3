from itertools import groupby
lis = [1, 2, 2, 3, 4, 4, 4, 4]
print(list(groupby(lis)))

things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"), ("vehicle", "school bus")]

for key, group in groupby(things, lambda x: x[0]):
    for thing in group:
        print("A %s is a %s." % (thing[1], key))
    print(" ")

for key, group in groupby(lis, lambda x:x):
    count = 0
    for item in group:
        count += 1
    print("The key is "+ str(key) +" the count is "+str(count))
