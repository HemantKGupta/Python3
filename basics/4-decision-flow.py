var = 100

if var == 100: print("Value of expression is 100")

speed = 85
mood = ''

if speed >= 80:
    print('License and registration please')
    if mood == 'terrible' or speed >= 100:
        print('You have the right to remain silent.')
    elif mood == 'bad' or speed >= 90:
        print("I'm going to have to write you a ticket.")
    else:
        print("Let's try to keep it under 80 ok?")



count = 0
while count < 2:
    print('The count is:', count)
    count += 1

# While with else
count = 0
while count < 3:
    print(count, " is  less than 5")
    count += 1
else:
    print(count)

# For
for letter in 'Python':
    print('Current Letter :', letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:
    print('Current fruit :', fruit)

# Break
for letter in 'Python':
    if letter == 'h':
        break
    print('Current Letter :', letter)

var = 10
while var > 0:
    print('Current variable value :', var)
    var -= 1
    if var == 5:
        break

# continue - start executing the loop with next code executioin
for letter in 'Python':     # First Example
    if letter == 'h':
        continue
    print('Current Letter :', letter)

var = 10
while var > 0:
    var -= 1
    if var == 5:
        continue
    print('Current variable value :', var)

# pass
for letter in 'Python':
    if letter == 'h':
        pass
        print('This is pass block')
    print('Current Letter :', letter)
