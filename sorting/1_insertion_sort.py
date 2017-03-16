def insertion_sort(a):
    for i in range(1, len(a)):
        value = a[i]
        hole = i
        while hole > 0 and a[hole-1] > value:
            a[hole] = a[hole-1]
            hole -= 1
        a[hole] = value


def insertion_sort2(l):
    for i in range(1, len(l)):
        j = i
        key = l[i]
        while (j > 0) and (l[j-1] > key):
           l[j] = l[j-1]
           j -= 1
        l[j] = key

def insertion_sort_swaps(input_array):
    swaps = 0
    for i in range(1, len(input_array)):
        value = input_array[i]
        hole = i
        while hole > 0 and input_array[hole - 1] > value:
            input_array[hole] = input_array[hole - 1]
            hole -= 1
            swaps += 1
        input_array[hole] = value
    return swaps


def insertion_sort_with_print(input_array):
    n = len(input_array)
    temp = input_array[n-1]
    placed = False
    for i in range(n - 2, -1, -1):
        element = input_array[i]
        if element > temp:
            input_array[i + 1] = element
        else:
            input_array[i + 1] = temp
            placed = True

        for item in range(0, n):
            print(input_array[item], end=" ")
        print()
        if (placed):
            break

    if not placed:
        input_array[0] = temp
        for item in range(0, n):
            print(input_array[item], end=" ")

a = [7, 2, 4, 1, 5, 3]
print(a)
insertion_sort(a)
print(a)
a = [7, 2, 4, 1, 5, 3]
print(insertion_sort_swaps(a))
