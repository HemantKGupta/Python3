# Import the numpy package as np
import numpy as np

weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]


np_weight = np.array(weight)

print(np_weight)

my_mat = [[1,2,3], [3,4,5], [6,7,8]]
np_my_mat = np.array(my_mat)
print(np_my_mat)

print(np.arange(0,10))

print(np.zeros(3))

print(np.linspace(1,5,5))
print(np.linspace(1,5,10))

print(np.random.rand(5))
print(np.random.rand(5,5))

print(np.random.randn(2))
