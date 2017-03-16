import numpy as np

# Make numpy array from a the list
print(np.array([1,2,3]))

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(np.array(my_matrix))

# create an array of items 0 to 10 (
print(np.arange(0,11))  # Check the last argument's value
print(np.arange(11))

# Create an array of the integers from 10 to 50
print(np.arange(10,50))

#You can provide the step also
print(np.arange(0,11,2))

# An array of zeros
print(np.zeros(3))

# Create the metrix of zeros
print(np.zeros((5,5)))

print(np.ones(3))

# create an array of 10 fives
print(5*np.ones(10))

# create 3 items from 0 to 10 equally spaced
print(np.linspace(0,10,3)) # [  0.   5.  10.]

# Identity metrix
print(np.eye(4))

# Two random numbers uniformally distributed between 0 and 1
print(np.random.rand(2))

print(np.random.rand(5,5))

# Standard normal distribution
print(np.random.randn(2))

# create a random number between 1 to 100
print(np.random.randint(1,100))

# Create 10 random number betwee 1 to 100
print(np.random.randint(1,100,10))

arr = np.arange(25) # 0 to 24
print(arr.reshape(5,5))

# 10 random numbers between 0 to 50
ranarr = np.random.randint(0,50,10)
print(ranarr)

# Max value in the array
print(ranarr.max())

# Index of the max
print(ranarr.argmax())


