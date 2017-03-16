import numpy as np
arr = np.arange(0,11)
print(arr)
print(arr[8])

print(arr[1:5])

print(arr[0:5])

arr[0:5]=100
print(arr)

arr = np.arange(0,11)
slice_of_arr = arr[0:6]
print(slice_of_arr)

slice_of_arr[:]=99
print(slice_of_arr)

arr_copy = arr.copy()
print(arr_copy)

arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))#Show

# Complete row
print(arr_2d[1])
# One item in two different way
print(arr_2d[1][0])
print(arr_2d[1,0])

print(arr_2d[:2,1:])
print(arr_2d[2])
print(arr_2d[2,:])

arr2d = np.zeros((10,7))
arr_rows = arr2d.shape[0]
print("array rows " + str(arr_rows))
arr_columns = arr2d.shape[1]
print("array columns "+str(arr_columns))

for i in range(arr_rows):
    arr2d[i] = i
    
print(arr2d)


# Fancy indexing allows the following
# fetch rows 2, 4, 6, 8
print(arr2d[[2,4,6,8]])

#Allows in any order
print(arr2d[[6,4,2,7]])


arr = np.arange(1,11)
bool_arr = arr>4
print(bool_arr)
print(arr[arr>2])

mat = np.arange(1,26).reshape(5,5)
print(mat)
print(mat[2:,1:])
print(mat[3][4])
print(mat[0:3,1:2])
print(mat[4])
print(mat[3:])
print(mat.sum())

