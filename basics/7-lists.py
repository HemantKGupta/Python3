list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5];
list3 = ["a", "b", "c", "d"]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

# update
list2[2] = 2001
print("list2[1:5]: ", list2[1:5])

# delete
del list1[2];
print("list: ", list1)

squares = [1, 4, 9, 16]

sum = 0
for num in squares:
    sum += num
print(sum)

testList = ['larry', 'curly', 'moe']
if 'curly' in testList:
    print('yay')

for i in range(100):
    print(i)
aTestList = ['larry', 'curly', 'moe']
aTestList.append('shemp')         ## append elem at end
aTestList.insert(0, 'xxx')        ## insert elem at index 0
aTestList.extend(['yyy', 'zzz'])  ## add list of elems at end

print(aTestList)
print(aTestList.index('curly'))    ## 2

aTestList.remove('curly')         ## search and remove that element
aTestList.pop(1)                  ## removes and returns 'larry'
print(aTestList)

newList = ['a', 'b', 'c', 'd']
print(newList[1:-1])

nest = [1,2,[3,4]]
print(nest[2][1]) # 4

lista = [1,2,3,4,5,6]
listb = [8,9]
lista[3:5] = listb
print(lista)
