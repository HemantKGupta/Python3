result = [1, 1, 1, 1, 1, 1, 1, 1]
def mergeLists(left, right):
    nL = len(left)
    nR = len(right)
    i=j=k=0
    while i < nL and j < nR:
        if left[i] <= right[j]:
            result[k] = left[i]
            i = i +1
            k = k + 1
        else:
            result[k] = right[j]
            j = j + 1
            k = k + 1
    while i < nL:
        result[k] = left[i]
        i = i + 1
        k = k + 1

    while j < nR:
        result[k] = right[j]
        j = j + 1
        k = k + 1

    print(result)

def mergeSort(input):
    length = len(input)
    mid = int(length/2)
    if length > 2:
        mergeSort(input[0:mid])
        mergeSort(input[mid:])
        mergeLists(input[0:mid], input[mid:])
    else:
        mergeLists(input[0:mid], input[mid:])

input = [2, 9, 6, 8, 1, 3, 5, 7]

mergeSort(input)


