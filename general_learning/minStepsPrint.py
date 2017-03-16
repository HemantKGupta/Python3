#!/usr/bin/python3
__author__ = 'hemant'
def printMinSteps(x):
		if (x==0):return
		if (x%2 == 0):
			printMinSteps(x/2)
			print("Double")
		else:
			printMinSteps(x-1)
			print("Increment")
print(printMinSteps(15))