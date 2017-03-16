#!/usr/bin/python3
__author__ = 'hemant'
def getMinSteps(x):
	counter = 0
	while (x>0):
		if (x%2 == 0):
			x= x/2
		else:
			x= x-1
		counter = counter + 1
	return counter	
print(getMinSteps(15))