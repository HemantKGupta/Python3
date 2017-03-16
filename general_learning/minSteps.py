#!/usr/bin/python3
__author__ = 'hemant'
x = 15
counter = 0
while (x>0):
	if (x%2 == 0):
		x= x/2
	else:
		x= x-1
	counter = counter + 1
print(counter)	