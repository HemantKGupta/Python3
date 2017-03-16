counter = 100          # An integer assignment
miles = 1000.0       # A floating point
name = "John"       # A string

print(miles)
print(name)
print(counter)

# Multiple assignment
a = b = c = 1
print(a,b,c)
a, b, c = 1, 2, "john"
print(a,b,c)

# Standard data types
#1 Numbers
var1 = 1
var3 = 2.3
var4 = 3.14j
del var1
print(var4, var3)

#2 String

aString = 'Hello World!'

print(aString) # Prints complete string
print(aString[0]) # Prints first character of the string
print(aString[2:5]) # Prints characters starting from 3rd to 5th
print(aString[2:]) # Prints string starting from 3rd character
print(aString * 2) # Prints string two times
print(aString + "TEST") # Prints concatenated string


#3 List  - By square brackets

aList = ['abcd', 786 , 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(aList)# Prints complete list
print(aList[0])# Prints first element of the list
print(aList[1:3])# Prints elements starting from 2nd till 3rd
print(aList[2:])# Prints elements starting from 3rd element

print(tinylist * 2)# Prints list two times

print(aList + tinylist) # Prints concatenated lists

#4 Tuple      By () and cannot be updated

aTuple = ('abcd', 786 , 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print(aTuple)# Prints complete list
print(aTuple[0])# Prints first element of the list# Dictionary
print(aTuple[1:3])# Prints elements starting from 2nd till 3rd
print(aTuple[2:])# Prints elements starting from 3rd element

print(tinytuple * 2   )# Prints list two times
print(aTuple + tinytuple) # Prints concatenated list()

#5 Dictionary
aDict = {}
aDict['one'] = "This is one"
aDict[2] = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print(aDict['one']) # Prints value for 'one' key
print(aDict[2]) # Prints value for 2 key

print(tinydict) # Prints complete dictionary

print(tinydict.keys())# Prints all the keys

print(tinydict.values()) # Prints all the values

# TODO: Data Type Conversion

