a_list = [2, 1, 4, 5, 3, 7]
print(len(a_list))
for i in range(len(a_list), 0, -1):
    print("the i is " + str(i))
    maxIndex = 0
    for j in range(0, i):
        print("the inside j is " + str(j))
        if a_list[j] > a_list[maxIndex]:
            maxIndex = j
    print("the maxIndex is " + str(maxIndex))
    temp = a_list[i-1]
    a_list[i-1] = a_list[maxIndex]
    a_list[maxIndex] = temp
print(a_list)