aDict = {'Name': 'Zara', 'Age': 7, 'Class': 'First', 1: 'test'}

print("dict['Name']: ", aDict['Name'])
print("dict['Age']: ", aDict['Age'])
print("dict[1]: ", aDict[1])

# update existing entry
aDict['Age'] = 8;
# Add new entry
aDict['School'] = "DPS School";


print("dict['Age']: ", aDict['Age'])
print("dict['School']: ", aDict['School'])

# remove entry with key 'Name'
del aDict['Name'];

# remove all entries in dict
#aDict.clear();
#delete entire dictionary
#del dict ;

#print("dict['Age']: ", aDict['Age'])


## By default, iterating over a dict iterates over its keys.
## Note that the keys are in a random order.
for key in aDict:
    print(key)

print(aDict.keys())
print(aDict.values())

for k, v in aDict.items():
    print(k, '>', v)

nest = {'key1':[1,2,3]}
print(nest['key1'])

