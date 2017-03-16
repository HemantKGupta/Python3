def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return
printme("Hi")

# Pass reference

def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print("Values outside the function: ", mylist)

# Function definition is here
def changeme2( mylist2 ):
    mylist2 = [1, 2, 3, 4];  # This would assig new reference in mylist
    print("Values inside the function: ", mylist2)
    return

# Now you can call changeme function
mylist2 = [10,20,30];
changeme2(mylist2);
print("Values outside the function: ", mylist2)


# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )

# Function definition is here
def printinfo2( name, age = 35 ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age ", age)
   return;

# Now you can call printinfo function
printinfo2(age=50, name="miki")
printinfo2(name="miki")


# variable length Function definition is here
def printinfo3( arg1, *vartuple ):
   print("Output is: ")
   print(arg1)

   for var in vartuple:
      print(var)
   return;

# Now you can call printinfo function
printinfo3(10)
printinfo3(70, 60, 50)

# lambda Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print("Value of total : ", sum(10, 20))
print("Value of total : ", sum(20, 20))