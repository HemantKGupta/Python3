n = int(input())
input_data = input()
input_array_list = input_data.split(' ')
input_array = list(map(int, input_array_list))
temp = input_array[n-1]
placed = False
for i in range(n-2, -1, -1):
    element = input_array[i]
    if element > temp:
        input_array[i+1] = element
    else:
        input_array[i+1] = temp
        placed = True

    for item in range(0, n):
        print(input_array[item], end=" ")
    print()
    if(placed):
        break

if not placed:
    input_array[0] = temp
    for item in range(0, n):
        print(input_array[item], end=" ")