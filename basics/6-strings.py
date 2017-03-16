var1 = 'Hello World!'
var2 = "Python Programming"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])

# Update
var1 = 'Hello World!'

print("Updated String :- ", var1[:6] + 'Python')

# format
print ("My name is %s and weight is %d kg!" % ('Zara', 21))

# Find
str1 = "this is string example....wow!!!";
str2 = "exam";

print(str1.find(str2))
print(str1.find(str2, 10))
print(str1.find(str2, 40))

a = "Hi"
a = a + str(len(a))
print(a)

s = 'hi'
print(s[1]          )## i
print(len(s)        )## 2
print(s + ' there')  ## hi there

pi = 3.14
##text = 'The value of pi is ' + pi      ## NO, does not work
text = 'The value of pi is ' + str(pi)  ## yes
print(text)
print('aaa,bbb,ccc'.split(','))

print('---'.join(['aaa', 'bbb', 'ccc']))
print(''.join(['aaa', 'bbb', 'ccc']))

print('My number is {} and my name is {}'.format(23, 'hemant'))
print('My number is {one} and my name is {two}'.format(one=23, two='hemant'))

