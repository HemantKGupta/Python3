#!/usr/bin/python3
__author__ = 'hemant'
def getMinStepsRecursively(x):
		if (x==0): return 0
		if (x%2 == 0):
			return 1 + getMinStepsRecursively(x/2)
		else:
			return 1 + getMinStepsRecursively(x-1)
print(getMinStepsRecursively(15))