def quicksort(array, lo, hi):
    if lo < hi:
        p = partition(array, lo, hi)
        for item in range(0, len(ar)):
            print(array[item], end=" ")
        print()
        quicksort(array, lo, p-1)
        quicksort(array, p + 1, hi)

def partition(array, lo, hi):
    pivot = array[hi]
    i = lo - 1
    for j in range(lo,hi):
        if array[j] <= pivot:
            i += 1
            swap(array, i, j)
    swap(array, i+1, hi)
    return i+1

def swap(array, first, second):
    temp = array[first]
    array[first] = array[second]
    array[second] = temp

def partition_basic(array):
    pivot = array[0]
    left = []
    right = []
    for i in range (1, len(array)):
        if array[i] < pivot:
            left.append(array[i])
        elif array[i] > pivot:
            right.append(array[i])
    print(" ".join(map(str,left)) + " "+str(pivot) + " " + " ".join(map(str,right)))

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
#partition(ar)

#print(get_partition_index(ar, 0, len(ar)-1))
#print(ar)
quicksort(ar, 0, len(ar)-1)
#print(ar)
