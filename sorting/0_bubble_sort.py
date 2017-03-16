a_list = [2, 1, 4, 5, 3, 7]
print(len(a_list))
for i in range(len(a_list)-1, 0, - 1):
    print("working for i " + str(i))
    for j in range(0, i):
        print("working inside for j " + str(j))
        if a_list[j+1] < a_list[j]:
            temp = a_list[j+1]
            a_list[j+1] = a_list[j]
            a_list[j] = temp

print(a_list)
